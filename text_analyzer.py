# text_analyzer.py
def analyze_symptom(text: str):
    """Simple text-based symptom checker using keyword rules."""
    text = text.lower()

    if any(k in text for k in ["itch", "rash"]):
        result = "Possible skin irritation or allergy."
    elif any(k in text for k in ["pain", "swelling"]):
        result = "Possible inflammation or mild infection."
    elif "mole" in text or "spot" in text:
        result = "Monitor the spot; if it changes, seek medical review."
    else:
        result = "Unable to classify symptom. Please provide more details."

    advisory = "This is not a diagnosis. Consult a qualified professional."
    return {"input": text, "analysis": result, "advisory": advisory}


def analyze_symptom(text: str):
    if not text:
        return {"analysis": "No symptom provided."}
    if "fever" in text.lower() or "headache" in text.lower():
        return {"analysis": "Possible mild infection. Rest and hydrate."}
    return {"analysis": "No concerning symptoms detected."}
