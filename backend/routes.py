from fastapi import APIRouter

from backend.schemas import ParcelRequest

from models.predict import predict_crop
from models.moisture import estimate_moisture
from models.weather import get_weather
from models.advisor import smart_advisor

router = APIRouter()


@router.post("/predict")
def predict(request: ParcelRequest):

    crop_label, crop_name, confidence = predict_crop(request.parcel_id)

    moisture = estimate_moisture(request.parcel_id)

    weather = get_weather()

    recommendation = smart_advisor(
        crop_name,
        moisture,
        weather
    )

    return {
        "parcel_id": request.parcel_id,

        "crop_label": crop_label,
        "crop_name": crop_name,
        "confidence": confidence,

        "moisture": moisture,

        "temperature": weather["temperature"],
        "humidity": weather["humidity"],
        "rainfall": weather["rain"],

        "recommendation_en": recommendation["english"],
        "recommendation_hi": recommendation["hindi"]
    }