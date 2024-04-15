from fastapi import FastAPI
from pydantic import BaseModel
import model_utils

app = FastApi()
model_utils.load_model()

class FeaturesInput(BaseModel):
    budget:float
    compositeur: str
    date:
    franchise: str
    genre: str
    pays: str
    producteur: str
    remake: str
    titre: str
    season: str
    coeff_studio: int
    scoring_acteurs&realisateur:
    pass


class PredictionOutput(BaseModel):
    entrees_premiere_semaine: int


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
    F12 = feature_input.scoring_acteurs&realisateur
    pred = model_utils.prediction(model, [[F1, F2, F3, F4, F5, F6, F7, F8]])

    return PredictionOutput(category=pred)

