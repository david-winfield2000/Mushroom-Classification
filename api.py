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

# Load expected feature columns
X_columns = joblib.load("X_columns.pkl")


@app.post("/classify", response_model=PredictionResponse)
def classify(mushroom: MushroomFeatures):
    # Convert Pydantic model to DataFrame
    df = pd.DataFrame([mushroom.dict()])

    # Use the same one-hot encoding as training
    df_encoded = pd.get_dummies(df)

    # Align columns with training set
    df_encoded = df_encoded.reindex(columns=X_columns, fill_value=0)

    # Predict
    pred = rf.predict(df_encoded)[0]

    return {"prediction": pred}
