# ethics_filter.py
import re
from typing import Optional

# Precompile patterns for performance and clarity
_PATTERNS = [
    # You're/you are + (confirmed to have | infected with | positive | tested positive)
    re.compile(r"\byou(?:'re|\s+are)\s+(?:confirmed\s+to\s+have|infected\s+with|positive\b|positive\s+for|tested\s+positive)\b", re.I),
    # You tested positive / you have tested positive
    re.compile(r"\byou(?:\s+have)?\s+tested\s+positive\b", re.I),
    # tested positive (general)
    re.compile(r"\btested\s+positive\b", re.I),
    # positive for <disease>
    re.compile(r"\bpositive\s+for\b", re.I),
    # It has been confirmed / It is confirmed / has been confirmed / was confirmed
    re.compile(r"\b(?:it\s+(?:has|is)\s+been\s+confirmed|has\s+been\s+confirmed|was\s+confirmed|confirmed\s+to\s+have)\b", re.I),
    # direct "you are infected with X"
    re.compile(r"\byou\s+are\s+infected\s+with\b", re.I),
]

def safe_output(text: Optional[str]) -> str:
    """
    Replace strongly deterministic/confirmatory medical statements with
    a neutral advisory. Case-insensitive, regex-based matching for common
    confirmatory phrasing (including contractions and 'tested positive' variants).

    Returns the original text if no unsafe phrase is found.
    """
    if text is None:
        return ""

    # Ensure we are working with a string
    if not isinstance(text, str):
        text = str(text)

    lowered = text.lower()

    for pat in _PATTERNS:
        if pat.search(lowered):
            return "Visit a doctor for confirmation."

    return text





# def safe_output(text: str):
#     ### Replacing unsafe wording with neutral advisory text
#     unsafe_words = ["you are confirmed to have", "You are infected with", "It has been confirmed", " You are positive"]
#     lowered = text.lower()

#     if any(word in lowered for word in unsafe_words):
#         return "Visit a Doctor for confirmation."

#     return text
