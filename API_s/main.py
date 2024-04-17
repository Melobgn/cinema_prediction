from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction
import pandas as pd

app = FastAPI()
model=load_model()


class FeaturesInput(BaseModel):
    budget:float
    duree: int
    franchise: str
    genre: str
    pays: str
    remake: str
    salles_premiere_semaine: int
    scoring_acteurs_realisateurs: float
    coeff_studio: int
    year: int

    

class PredictionOutput(BaseModel):
    prediction: float

@app.post('/prediction/')
def prediction_root(feature_input: FeaturesInput):
    F1 = feature_input.budget
    F2 = feature_input.duree
    F3 = feature_input.franchise
    F4 = feature_input.genre
    F5 = feature_input.pays
    F6 = feature_input.remake
    F7 = feature_input.salles_premiere_semaine
    F8 = feature_input.scoring_acteurs_realisateurs
    F9 = feature_input.coeff_studio
    F10 = feature_input.year

    data = pd.DataFrame([[F1, F2, F3, F4, F5, F6, F7, F8, F9, F10]], columns=['budget', 'duree', 'franchise', 'genre', 'pays', 'remake', 'salles_premiere_semaine', 'scoring_acteurs_realisateurs', 'coeff_studio', 'year'])
    predictions = model.predict(data)

    return PredictionOutput(prediction=predictions)

# actors = pd.read_csv('acteurs.csv')

# def calcul_poids_total(casting: FeaturesInput, realisateur: FeaturesInput):
#     poids_total = 0
#     casting = list(casting.split(", ")) 
    
#     for i in range (len(casting)): 
#         if casting[i] in actors['name'].values: #si acteur[indice] se trouve dans la colonne 'name' du dataframe 'acteurs'
#             poids_acteur = actors.loc[actors['name'] == casting[i], 'coef_poids'].values[0]  # Récupérer le poids de l'acteur
#             poids_total += poids_acteur  # Multiplie le poids de l'acteur par la valeur présente dans poids_total

#     if realisateur in actors['name'].values:
#         poids_realisateur = actors.loc[actors['name'] == realisateur, 'coef_poids'].values[0]
#         poids_total += poids_realisateur

#     return poids_total

# #route api pour effectuer calcul et renvoyer le résultat
# @app.post("/prediction/")
# async def prediction (data: FeaturesInput):
#     score_acteurs_realisateur = calcul_poids_total(data)