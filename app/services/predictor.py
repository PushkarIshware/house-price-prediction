import pickle
import joblib
import pandas as pd
from app.schemas import HouseDataInput

class PredictorService:
    def __init__(self):
        self.model_path = "ai_model/RF-model.pkl"
        # self.scaler_path = "ai_model/RF_scaler.pkl"

        self.model = joblib.load(self.model_path)
        # self.scaler = joblib.load(self.scaler_path)

        # with open(self.model_path, "rb") as f:
        #     self.model = pickle.load(f)

        # with open(self.scaler_path, "rb") as f:
        #     self.scaler = pickle.load(f)

    def predict_price(self, data: HouseDataInput) -> float:
        input_df = pd.DataFrame([data.dict()])
        # input_scaled = self.scaler.transform(input_df)
        prediction = self.model.predict(input_df)
        return prediction[0]
