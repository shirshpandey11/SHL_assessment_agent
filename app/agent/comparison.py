from app.catalog.loader import load_catalog


def compare_assessments(names):

    catalog = load_catalog()

    matches = []

    for assessment in catalog:

        for name in names:

            if name.lower() in assessment.name.lower():
                matches.append(assessment)
                break

    if len(matches) == 0:
        return (
            "I couldn't find those assessments in the SHL catalog. "
            "Please use the exact assessment names."
        )

    if len(matches) == 1:

        a = matches[0]

        return f"""
Assessment Found

Name:
{a.name}

Categories:
{", ".join(a.categories)}

Job Levels:
{", ".join(a.job_levels)}

Description:
{a.description}

URL:
{a.url}
"""

    a = matches[0]
    b = matches[1]

    return f"""
Comparison

------------------------------------------------

{a.name}

Categories:
{", ".join(a.categories)}

Job Levels:
{", ".join(a.job_levels)}

Description:
{a.description}

------------------------------------------------

{b.name}

Categories:
{", ".join(b.categories)}

Job Levels:
{", ".join(b.job_levels)}

Description:
{b.description}
"""