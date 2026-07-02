import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from app.catalog.loader import load_catalog
from app.models.assessment import Assessment


class EmbeddingRetriever:
    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.catalog = load_catalog()

        self.documents = [
            assessment.searchable_text
            for assessment in self.catalog
        ]

        print("Generating embeddings...")

        embeddings = self.model.encode(
            self.documents,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        self.embeddings = embeddings.astype("float32")

        dimension = self.embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(self.embeddings)

        print(f"Indexed {len(self.catalog)} assessments.")

    def search(
        self,
        query: str,
        top_k: int = 10
    ) -> list[Assessment]:

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True
        ).astype("float32")

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        return [
            self.catalog[i]
            for i in indices[0]
        ]