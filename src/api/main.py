# src/api/main.py
from fastapi import FastAPI
from src.api.pydantic_models import CustomerData, PredictionResponse
import mlflow.pyfunc
import numpy as np

# Load model from MLflow registry
model = mlflow.pyfunc.load_model(model_uri="models:/rfm_credit_model/Production")

app = FastAPI(title="Credit Risk Scoring API")

@app.post("/predict", response_model=PredictionResponse)
def predict(data: CustomerData):
    features = np.array([[data.recency, data.frequency, data.monetary]])
    prediction = model.predict(features)[0]
    probability = float(prediction)  # If model outputs prob
    return {"risk_score": probability, "creditworthy": "Yes" if probability > 0.5 else "No"}
