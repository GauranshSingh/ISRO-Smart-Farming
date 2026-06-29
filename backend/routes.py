from fastapi import APIRouter

from backend.schemas import FieldRequest, PredictionResponse

from models.advisor import smart_advisor

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: FieldRequest):

    report = smart_advisor(request.field_id)

    return report
