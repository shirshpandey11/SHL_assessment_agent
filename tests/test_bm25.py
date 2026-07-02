from app.retrieval.bm25 import BM25Retriever

retriever = BM25Retriever()

query = "Java developer"

results = retriever.search(query, top_k=5)

print("=" * 60)
print(f"Query: {query}")
print("=" * 60)

for i, assessment in enumerate(results, start=1):
    print(f"\n{i}. {assessment.name}")
    print(assessment.url)