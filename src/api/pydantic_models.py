# src/api/pydantic_models.py
from pydantic import BaseModel

class CustomerData(BaseModel):
    recency: float
    frequency: float
    monetary: float

class PredictionResponse(BaseModel):
    risk_score: float
    creditworthy: str
