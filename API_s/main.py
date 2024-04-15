from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction
import pandas as pd

app = FastApi()
model=load_model()


class FeaturesInput(BaseModel):
    budget:float
    compositeur: str
    date: str
    franchise: str
    genre: str
    pays: str
    producteur: str
    remake: str
    titre: str
    season: str
    coeff_studio: int
    scoring_acteurs_realisateur: float
    

class PredictionOutput(BaseModel):
    prediction: int


def prediction_root(feature_input: FeaturesInput):
    F1 = feature_input.budget
    F2 = feature_input.compositeur
    F3 = feature_input.date
    F4 = feature_input.franchise
    F5 = feature_input.genre
    F6 = feature_input.pays
    F7 = feature_input.producteur
    F8 = feature_input.remake
    F9 = feature_input.titre
    F10 = feature_input.season
    F11 = feature_input.coeff_studio
    F12 = feature_input.scoring_acteurs_realisateur

    prediction = model.prediction(model, [[F1, F2, F3, F4, F5, F6, F7, F8]])

    return PredictionOutput(category=prediction)


def 