import pickle

import joblib
import pandas as pd
from fastapi import FastAPI

from schema import MushroomFeatures, PredictionResponse

app = FastAPI(
    title="Mushroom Classifier API",
    description="Classify mushrooms as edible ('e') or poisonous ('p') based on their features.",
)

# Load trained model
with open("rf_model.pkl", "rb") as f:
    rf = pickle.load(f)


@app.post("/classify", response_model=PredictionResponse)
def classify(mushroom: MushroomFeatures):
    print(mushroom)
    return {"prediction": "HAHA I am a joke, I don't know how to classify mushrooms!"}
