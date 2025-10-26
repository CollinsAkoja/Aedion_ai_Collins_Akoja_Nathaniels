# ethics_filter.py
def safe_output(text: str):
    ### Replacing unsafe wording with neutral advisory text
    unsafe_words = ["you are confirmed to have", "You are infected with", "It has been confirmed", " You are positive"]
    lowered = text.lower()

    if any(word in lowered for word in unsafe_words):
        return "Visit a Doctor for confirmation."

    return text
