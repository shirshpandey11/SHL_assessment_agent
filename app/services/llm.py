import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_reply(query: str, recommendations: list[str]) -> str:
    """
    Generate a natural language response using Gemini.
    Recommendations are already selected by the retriever.
    """

    prompt = f"""
You are an SHL Assessment recommendation assistant.

The retrieval system has already selected the assessments.

User Requirement:
{query}

Selected Assessments:
{chr(10).join("- " + r for r in recommendations)}

Instructions:
- Do NOT invent assessments.
- Mention ONLY the assessments provided.
- Explain briefly why they fit.
- Keep the response under 120 words.
- Be professional and concise.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return (
            "Based on your requirements, I've selected the most relevant SHL "
            "assessments from the catalog."
        )