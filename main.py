from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load the persisted model
model = joblib.load("car-recommender.joblib")

# Initialize FastAPI
app = FastAPI()

# Define the input data structure
class CarFeatures(BaseModel):
    feature_1: float
    feature_2: float

@app.post("/predict")
def predict_car_type(features: CarFeatures):
    # Prepare input data for prediction
    input_data = [[features.feature_1, features.feature_2]]
    prediction = model.predict(input_data)
    
    return {"predicted_vehicle_type": prediction[0]}
