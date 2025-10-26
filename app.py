# app.py
# AedionAI Basic Project - Flask AI API
# Author: Collins Akoja Nathaniels

from flask import Flask, request, jsonify
from image_classifier import analyze_image
from text_analyzer import analyze_symptom
from ethics_filter import safe_output
import time, os

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return jsonify({
        "message": " Aedion Basic AI API is running successfully",
        "endpoints": ["/analyze_image", "/analyze_text"],
        "note": "Send an image or text symptom to receive a quick AI advisory"
    })


#  Image Analyzer Endpoint
@app.route("/analyze_image", methods=["POST"])
def analyze_img():
    if "image" not in request.files:
        return jsonify({"error": "Please upload an image file"}), 400

    start = time.time()
    file = request.files["image"]
    temp_path = "temp_input.jpg"
    file.save(temp_path)

    result = analyze_image(temp_path)
    result["advisory"] = safe_output(result["advisory"])
    result["time_taken_sec"] = round(time.time() - start, 3)

    os.remove(temp_path)
    return jsonify(result)


#  Text Analyzer Endpoint
@app.route("/analyze_text", methods=["POST"])
def analyze_txt():
    try:
        data = request.get_json(force=True)
        symptom_text = data.get("symptom", "").strip()
    except:
        return jsonify({"error": "Please provide valid JSON input"}), 400

    start = time.time()
    result = analyze_symptom(symptom_text)
    result["analysis"] = safe_output(result["analysis"])
    result["time_taken_sec"] = round(time.time() - start, 3)

    return jsonify(result)


#  Run the app
if __name__ == "__main__":
    app.run(debug=True)
