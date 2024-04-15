from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .movie_prediction import predict_movie

# créeer une instance de FastAPI

app = FastAPI()

## Middleware CORS pour permettre les requêtes depuis n'importe quel domaine (à adapter selon vos besoins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Définition des endpoints

# Utilisez GET pour read_root() car vous voulez que les utilisateurs récupèrent des informations sur l'API.
@app.get("/")
async def read_root():
    return {"message":"Bienvenue sur votre API de prédiction de films"}



# Utilisez POST pour predict() car vous voulez que les utilisateurs envoient des données 
# (les informations nécessaires pour faire une prédiction) au serveur pour traitement.
@app.post("/predict")
async def predict(data: dict):
    prediction = predict_movie(data)
    return {"prediction":prediction}

    # Utilisez GET lorsque vous souhaitez récupérer des données existantes depuis le serveur, par exemple
    #  pour afficher une page ou obtenir des informations.

    # Utilisez POST lorsque vous souhaitez envoyer des données au serveur pour traitement, par exemple 
    # pour soumettre un formulaire ou créer une nouvelle ressource.

