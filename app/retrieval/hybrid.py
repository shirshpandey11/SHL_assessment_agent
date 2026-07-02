from app.retrieval.bm25 import BM25Retriever


class HybridRetriever:
    """
    Lightweight retriever for deployment.

    Uses BM25 only to avoid loading large embedding models.
    """

    def __init__(self):
        print("Initializing BM25 Retriever...")
        self.bm25 = BM25Retriever()

    def search(self, query: str, top_k: int = 7):
        return self.bm25.search(
            query=query,
            top_k=top_k,
        )
