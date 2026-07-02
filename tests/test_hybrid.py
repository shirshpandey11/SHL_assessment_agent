from app.retrieval.hybrid import HybridRetriever

retriever = HybridRetriever()

query = "Hiring a Java backend developer"

results = retriever.search(query)

print("=" * 60)
print(query)
print("=" * 60)

for i, assessment in enumerate(results, start=1):

    print()

    print(i)
    print(assessment.name)
    print(assessment.url)

    