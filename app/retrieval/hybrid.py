from collections import defaultdict

from app.retrieval.bm25 import BM25Retriever
from app.retrieval.embeddings import EmbeddingRetriever
from app.models.assessment import Assessment


class HybridRetriever:
    """
    Hybrid search using Reciprocal Rank Fusion (RRF).

    Combines:
    - BM25 lexical search
    - FAISS semantic search
    """

    def __init__(self):

        print("Initializing BM25 Retriever...")
        self.bm25 = BM25Retriever()

        print("Initializing Embedding Retriever...")
        self.embedding = EmbeddingRetriever()

    def search(
        self,
        query: str,
        top_k: int = 10,
        rrf_k: int = 60,
    ) -> list[Assessment]:

        bm25_results = self.bm25.search(query, top_k=20)

        embedding_results = self.embedding.search(query, top_k=20)

        scores = defaultdict(float)

        assessment_lookup = {}

        # BM25 contribution
        for rank, assessment in enumerate(bm25_results):
            scores[assessment.id] += 1 / (rrf_k + rank + 1)
            assessment_lookup[assessment.id] = assessment

        # Embedding contribution
        for rank, assessment in enumerate(embedding_results):
            scores[assessment.id] += 1 / (rrf_k + rank + 1)
            assessment_lookup[assessment.id] = assessment

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            assessment_lookup[assessment_id]
            for assessment_id, _ in ranked[:top_k]
        ]
    
