from rank_bm25 import BM25Okapi
from app.utils.tokenizer import tokenize
from app.catalog.loader import load_catalog
from app.models.assessment import Assessment


class BM25Retriever:
    def __init__(self):
        # Load all assessments
        self.catalog = load_catalog()


        self.documents = [
            tokenize(assessment.searchable_text)
            for assessment in self.catalog
        ]

        # Build BM25 index
        self.bm25 = BM25Okapi(self.documents)

    def search(self, query: str, top_k: int = 10) -> list[Assessment]:
        """
        Search the SHL catalog using BM25.

        Args:
            query: User query.
            top_k: Number of results.

        Returns:
            List of Assessment objects.
        """

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked = sorted(
            zip(scores, self.catalog),
            key=lambda x: x[0],
            reverse=True,
        )

        return [
            assessment
            for score, assessment in ranked[:top_k]
            if score > 0
        ]
    
