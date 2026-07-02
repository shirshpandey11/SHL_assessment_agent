from app.catalog.loader import load_catalog

catalog = load_catalog()

print("=" * 50)
print(f"Loaded {len(catalog)} assessments")
print("=" * 50)

print("\nFirst Assessment:\n")
print(catalog[0])

print("\nSearchable Text:\n")
print(catalog[0].searchable_text)
