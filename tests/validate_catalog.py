import json
from pathlib import Path

CATALOG_PATH = Path("app/catalog/shl_catalog.json")

try:
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("✅ Valid JSON")
    print(f"Type: {type(data)}")
    print(f"Assessments: {len(data)}")

except json.JSONDecodeError as e:
    print("❌ JSON Error")
    print(e)