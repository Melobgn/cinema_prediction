import pandas as pd
import pickle

#chargement du modèle


def load_model(model_path='modele_api.pkl'):
    with open (model_path, 'rb') as file:
        model = pickle.load(file)
    return model



# Définissez une fonction pour effectuer des prédictions de films
def predict_movie(data,model):
    # Créez un DataFrame à partir des données reçues
    # df = pd.DataFrame(data, index=[0])
    new_films = pd.DataFrame(data)

# faire des prédictions avec le modèle optimisé
    new_y_pred = model.predict(new_films)

# Retourner les prédictions

    return new_y_pred

model= load_model()
data = {
    'titre': ['NOUS, LES LEROY'],
    'budget': [None],
    'genre': ['Comédie'],
    'pays': ['France'],
    'producteur': ['missing'],
    'realisateur': ['missing'],
    'compositeur': ['missing'],
    'studio': ['Apollo Films'],
    'coeff_studio': [1],
    'date': ['2024-04-10'],
    'season': ['Hiver'],
    'scoring_acteurs&realisateur': [0.5],
    'remake': [None],
    'franchise': [None],
}

predictions = predict_movie(data,model)

print(predictions)
    





    