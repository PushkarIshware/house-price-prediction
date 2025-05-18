from fastapi import APIRouter
from app.api import predict

router = APIRouter()

# include endpont logic here
router.include_router(predict.router, tags=["Predict"], prefix="/predict")
