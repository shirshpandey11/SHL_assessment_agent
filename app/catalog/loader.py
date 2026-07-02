import json
from pathlib import Path

from app.models.assessment import Assessment

# Path to the SHL catalog
CATALOG_PATH = Path("app/catalog/shl_catalog.json")


def load_catalog() -> list[Assessment]:
    """
    Load the SHL catalog from JSON and convert each record
    into an Assessment object.

    Returns:
        list[Assessment]: List of normalized assessment objects.
    """

    with open(CATALOG_PATH, "r", encoding="utf-8") as file:
        raw_catalog = json.load(file)

    assessments: list[Assessment] = []

    for item in raw_catalog:

        # Create a structured document for retrieval models
        searchable_text = f"""
Assessment Name:
{item.get("name", "")}

Description:
{item.get("description", "")}

Categories:
{' '.join(item.get("keys", []))}

Job Levels:
{' '.join(item.get("job_levels", []))}

Languages:
{' '.join(item.get("languages", []))}

Remote Testing:
{item.get("remote", "")}

Adaptive:
{item.get("adaptive", "")}

Duration:
{item.get("duration", "")}
""".strip()

        assessment = Assessment(
            id=str(item.get("entity_id", "")),
            name=item.get("name", ""),
            url=item.get("link", ""),
            description=item.get("description", ""),
            job_levels=item.get("job_levels", []),
            languages=item.get("languages", []),
            duration=item.get("duration", ""),
            remote=item.get("remote", "").lower() == "yes",
            adaptive=item.get("adaptive", "").lower() == "yes",
            categories=item.get("keys", []),
            searchable_text=searchable_text,
        )

        assessments.append(assessment)

    return assessments


if __name__ == "__main__":
    catalog = load_catalog()

    print("=" * 60)
    print(f"Loaded {len(catalog)} assessments")
    print("=" * 60)

    print("\nFirst Assessment:\n")
    print(catalog[0])