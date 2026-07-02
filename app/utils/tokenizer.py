import re

def tokenize(text: str) -> list[str]:
    """
    Clean and tokenize text for BM25 indexing.
    """

    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Split into tokens
    return text.split()