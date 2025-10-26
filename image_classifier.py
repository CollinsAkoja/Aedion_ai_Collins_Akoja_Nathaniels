# image_classifier.py
from PIL import Image
import numpy as np
import cv2
import os


def analyze_image(abnormal: str):
    ### Basic_ai image analyzer
    if not os.path.exists(abnormal):
        return {"error": "File not found"}

    img = Image.open(abnormal).convert("RGB")
    arr = np.array(img)

    mean_color = np.mean(arr)
    std_color = np.std(arr)
    edges = cv2.Canny(arr, 100, 200)
    edge_score = np.mean(edges)

    if edge_score > 40 and std_color > 50:
        label = "abnormal"
        advisory = "Possible irregular skin pattern. Please consult a dermatologist."
    else:
        label = "normal"
        advisory = "No major irregularities detected. Continue monitoring."

    return {
        "label": label,
        "mean_color": round(float(mean_color), 2),
        "edge_score": round(float(edge_score), 2),
        "advisory": advisory
    }


#  Load the image dataset
def load_images_from_folder(abnormal):
    images = []
    for filename in os.listdir(abnormal):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(abnormal,vitiligo-19.jpg)
            img = Image.open(img_path).resize((128, 128))
            images.append((filename, np.array(img)))
    return images

# #  Simple image classifier
# def classify_image(image_array):
#     # Randomly simulate a prediction score
#     confidence = round(random.uniform(0.5, 1.0), 2)
#     # If the mean brightness is low, assume "abnormal" for simulation
#     mean_brightness = np.mean(image_array)
#     if mean_brightness < 100:
#         diagnosis = "Possible Diabetic Retinopathy"
#         label = "Abnormal"
#     else:
#         diagnosis = "Normal"
#         label = "Normal"
#     return label, confidence, diagnosis
#
# #  Run the analysis
# def analyze_dataset():
#     normal_images = load_images_from_folder("dataset/normal")
#     abnormal_images = load_images_from_folder("dataset/abnormal")
#
#     all_images = normal_images + abnormal_images
#
#     print("<<Aedion AI Medical Image Analysis>>")
#     for filename, image_array in all_images:
#         label, confidence, diagnosis = classify_image(image_array)
#         print(f"{filename} → {label} ({confidence}) | {diagnosis}")
#
# if __name__ == "__main__":
#     analyze_dataset()
#
