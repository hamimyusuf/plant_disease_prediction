from fastapi import FastAPI
from routes.predict_route import router as PredictRouter

app = FastAPI(
    title='Plant Disease Detection'
)

app.include_router(PredictRouter, tags=["Predict Image Plant"],prefix="/predict")