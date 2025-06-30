from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("models/rfm_credit_classifier.pkl")

# Create API instance
app = FastAPI(title="Credit Risk API")

# Define input schema
class InputData(BaseModel):
    recency: float
    frequency: float
    monetary: float

# Define endpoint
@app.post("/predict")
def predict_risk(data: InputData):
    features = np.array([[data.recency, data.frequency, data.monetary]])
    prediction = model.predict(features)[0]
    return {
        "prediction": int(prediction),
        "creditworthy": "Yes" if prediction == 1 else "No"
    }
