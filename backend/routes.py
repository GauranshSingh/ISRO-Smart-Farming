from fastapi import APIRouter

from backend.schemas import ParcelRequest

from models.advisor import smart_advisor

router = APIRouter()


@router.post("/predict")
def predict(request: ParcelRequest):

    report = smart_advisor(request.parcel_id)

    return report