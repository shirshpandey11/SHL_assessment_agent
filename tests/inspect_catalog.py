import json
from pathlib import Path

CATALOG_PATH = Path("app/catalog/shl_catalog.json")

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 60)
print("JSON Type:", type(data))
print("=" * 60)

if isinstance(data, list):
    print(f"Total assessments: {len(data)}")

    print("\nFirst assessment:\n")
    print(data[0])

    print("\nAvailable fields:\n")
    print(list(data[0].keys()))
else:
    print("Top-level keys:")
    print(list(data.keys()))