import tensorflow as tf
import numpy as np
import cv2
import os
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity

# Load Pre-trained Model for Feature Extraction
base_model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")
model = Model(inputs=base_model.input, outputs=base_model.output)

def preprocess_image(img_path):
    """Preprocess fingerprint image for feature extraction"""
    img = cv2.imread(img_path, 0)
    img = cv2.resize(img, (224, 224))  # Resize to match MobileNetV2 input
    img = np.stack((img,) * 3, axis=-1)  # Convert grayscale to 3-channel RGB
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize
    return img

def extract_features(img_path):
    """Extract feature vector from fingerprint image"""
    img = preprocess_image(img_path)
    features = model.predict(img)
    return features.flatten()

def is_fingerprint_in_db(query_img_path, db_folder, threshold=0.8):
    """Compare query fingerprint with database fingerprints using deep learning"""
    query_features = extract_features(query_img_path)
    best_match = None
    max_similarity = 0

    for file in os.listdir(db_folder):
        db_img_path = os.path.join(db_folder, file)
        db_features = extract_features(db_img_path)
        
        # Compute Cosine Similarity
        similarity = cosine_similarity([query_features], [db_features])[0][0]

        if similarity > max_similarity:
            max_similarity = similarity
            best_match = file

        if similarity >= threshold:
            return True, best_match  # Fingerprint matched

    return False, None  # No match found

# # Example usage
# query_fingerprint = "Sudarsan_fingerprint.jpg"
# fingerprint_db_folder = "fingerprint_database"
# match_found, matched_file = is_fingerprint_in_db(query_fingerprint, fingerprint_db_folder)

# if match_found:
#     print(f"Fingerprint found! Matched with: {matched_file}")
# else:
#     print("Fingerprint not found in the database.")
