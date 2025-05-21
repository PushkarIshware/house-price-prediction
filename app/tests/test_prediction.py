import unittest
from app.schemas import HouseDataInput
from app.services.predictor import PredictorService

class TestPrediction(unittest.TestCase):
    
    def setUp(self):
        
        self.class_obj = PredictorService()

    def test_predict_valid_input(self):

        input_data = {
            "house_age": 100,
            "distance_to_mrt": 1,
            "num_convenience_stores": 0,
            "latitude": -90,
            "longitude": -180,
            "year": 2000,
            "month": 1,
            "day": 1
        }

        input_via_model = HouseDataInput(**input_data)

        result = self.class_obj.predict_price(input_via_model)
        
        self.assertEqual(result,26.9)

if __name__ == '__main__':
    unittest.main()