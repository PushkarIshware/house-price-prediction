from fastapi import APIRouter

from app.schemas import HouseDataInput
from app.services.predictor import PredictorService

router = APIRouter()

@router.post("")
async def predict_price(
    data: HouseDataInput, # request data body
):
    obj = PredictorService()
    predicted_price = obj.predict_price(data)
    return {"predicted_price_per_unit_area": round(predicted_price, 2)}
