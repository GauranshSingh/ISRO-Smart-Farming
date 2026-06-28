from pathlib import Path

import joblib
import pandas as pd

from models.feature_extractor import extract_features
from models.label_names import LABEL_NAMES

# =====================================================
# Paths
# =====================================================

ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = ROOT / "outputs" / "crop_classifier.pkl"

# =====================================================
# Load Model
# =====================================================

model = joblib.load(MODEL_PATH)

# =====================================================
# Prediction Function
# =====================================================

def predict_crop(parcel_id):

    # Extract Features
    features = extract_features(parcel_id)

    # Remove label because model predicts it
    features.pop("label", None)

    # Convert into DataFrame
    X = pd.DataFrame([features])

    # Predict Label
    prediction = int(model.predict(X)[0])

    # Predict Confidence
    confidence = float(model.predict_proba(X)[0].max() * 100)

    # Convert Label -> Crop Name
    crop_name = LABEL_NAMES.get(prediction, "Unknown Crop")

    return {
        "parcel_id": parcel_id,
        "label": prediction,
        "crop_name": crop_name,
        "confidence": confidence
    }


# =====================================================
# Example
# =====================================================

if __name__ == "__main__":

    parcel = 10011413

    result = predict_crop(parcel)

    print("\n========================================")
    print("        CROP PREDICTION RESULT")
    print("========================================\n")

    print(f"Parcel ID   : {result['parcel_id']}")
    print(f"Crop Label  : {result['label']}")
    print(f"Crop Name   : {result['crop_name']}")
    print(f"Confidence  : {result['confidence']:.2f}%")

    print("\n========================================")