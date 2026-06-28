from pydantic import BaseModel


class ParcelRequest(BaseModel):
    parcel_id: int


class PredictionResponse(BaseModel):
    parcel_id: int

    crop_label: int
    crop_name: str
    confidence: float

    moisture: float

    temperature: float
    humidity: float
    rainfall: float

    recommendation_en: str
    recommendation_hi: str