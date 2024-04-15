import pandas as pd
import pickle

#chargement du modèle

with open ('model.pkl', 'rb') as file:
    model = pickle.load(file)



# Définissez une fonction pour effectuer des prédictions de films
def predict_movie(data):
    # Créez un DataFrame à partir des données reçues
    df = pd.DataFrame(data, index=[0])


    # Effectuez la prédiction en utilisant le modèle chargé
    prediction = model.predict(df)

    return prediction