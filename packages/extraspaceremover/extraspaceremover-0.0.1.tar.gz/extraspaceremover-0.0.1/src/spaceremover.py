import re

def remove_extra_spaces(text: str) -> str:
    """Remove extra spaces from an input text

    Args:
        text (str): Input text

    Returns:
        str: Text without extra spaces
    """
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    text = text.strip()
    return text