# app.py
# AedionAI Basic Project - Flask AI API
# Author: Collins Akoja Nathaniels

from flask import Flask, request, jsonify
from image_classifier import analyze_image
from text_analyzer import analyze_symptom
from ethics_filter import safe_output
import time
import os
import tempfile

app = Flask(__name__)
# Optional: limit upload size (16 MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "Aedion Basic AI API is running successfully",
        "endpoints": ["/analyze_image", "/analyze_text"],
        "note": "Send an image or text symptom to receive a quick AI advisory"
    })


# Image Analyzer Endpoint
@app.route("/analyze_image", methods=["POST"])
def analyze_img():
    if "image" not in request.files:
        return jsonify({"error": "Please upload an image file"}), 400

    file = request.files["image"]
    # Basic mimetype check
    if not getattr(file, "mimetype", "").startswith("image/"):
        return jsonify({"error": "Uploaded file is not an image"}), 400

    start = time.time()

    # Use a unique temporary file to avoid collisions
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    temp_path = tmp.name
    tmp.close()

    try:
        file.save(temp_path)
        try:
            result = analyze_image(temp_path) or {}
        except Exception as e:
            return jsonify({"error": "Image analysis failed", "detail": str(e)}), 500

        if isinstance(result.get("advisory"), str):
            result["advisory"] = safe_output(result["advisory"])

        result["time_taken_sec"] = round(time.time() - start, 3)
        return jsonify(result)
    finally:
        # Ensure cleanup; ignore errors during cleanup
        try:
            if os.path.exists(temp_path):
                os.remove(temp_path)
        except Exception:
            pass


# Text Analyzer Endpoint
@app.route("/analyze_text", methods=["POST"])
def analyze_txt():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Please provide valid JSON input"}), 400

    symptom_text = (data.get("symptom") or "").strip()
    if not symptom_text:
        return jsonify({"error": "Please provide a non-empty 'symptom' field"}), 400

    start = time.time()
    try:
        result = analyze_symptom(symptom_text) or {}
    except Exception as e:
        return jsonify({"error": "Text analysis failed", "detail": str(e)}), 500

    if isinstance(result.get("analysis"), str):
        result["analysis"] = safe_output(result["analysis"])

    result["time_taken_sec"] = round(time.time() - start, 3)
    return jsonify(result)


# Run the app
if __name__ == "__main__":
    # Use host="0.0.0.0" if you need external access (containers/dev-boxes)
    app.run(host="0.0.0.0", debug=True)
