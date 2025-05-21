import pickle
import pandas as pd
from app.schemas import HouseDataInput

class PredictorService:
    def __init__(self):
        self.model_path = "ai_model/RF-model.pkl"

        with open(self.model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict_price(self, data: HouseDataInput) -> float:
        input_df = pd.DataFrame([data.dict()])
        # input_scaled = self.scaler.transform(input_df)
        prediction = self.model.predict(input_df)
        return prediction[0]
