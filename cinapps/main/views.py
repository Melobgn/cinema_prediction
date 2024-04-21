from django.shortcuts import render
from .functions import scoring_casting, get_studio_coefficient
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
import json
import mysql.connector
from .database import connect_to_azure_mysql, get_actors_by_film, get_directors_by_film
import requests
from datetime import datetime, timedelta
import pandas as pd 
from .models import PredictionFilm

#charger le csv
actors = pd.read_csv('main/acteurs_coef.csv')

@login_required
def home_page(request):
    conn = connect_to_azure_mysql()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT id_film, titre, studio, description, image, film_url, date_sortie, genre, salles, pays, duree, budget FROM films WHERE is_pred = %s"
            cursor.execute(query, (1,))
            films = cursor.fetchall()


            for film in films:
                film['acteurs'] = [actor['nom'] for actor in get_actors_by_film(conn, film['id_film'])]
                film['realisateurs'] = [director['nom'] for director in get_directors_by_film(conn, film['id_film'])]
                film['scoring_acteurs_realisateurs'] = scoring_casting(film, actors)
                film['coeff_studio'] = get_studio_coefficient(film['studio'], conn)

            cursor.close()
            conn.close()

            # Obtention des prédictions pour chaque film
            films = get_predictions(films)
            # Trier les films par prédiction d'entrées dans l'ordre décroissant
            films_sorted = sorted(films, key=lambda x: x.get('prediction_entrees', 0), reverse=True)
            
             # Sélectionner uniquement les dix meilleurs films
            top_ten_films = films_sorted[:10]
            
            # Sélectionner uniquement les deux premiers
            top_two_films = films_sorted[:2]
            
            #chiffre d'affaire
            ch_affaires = sum(film['estimation_recette_hebdo'] for film in top_two_films)
            charge = 4900
            benefice = ch_affaires - charge

            tab_result = {
                'ch_affaires':ch_affaires,
                'charge':charge,
                'benefice': benefice
            }

            return render(request, "main/home_page.html", {"films": top_ten_films, "top_two": top_two_films, "tab_result":tab_result})
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'exécution de la requête SQL: {e}")
            return render(request, 'main/home_page.html', {"error": str(e)})
    else:
        print("La connexion à la base de données n'a pas été établie avec succès.")
        return render(request, 'main/home_page.html', {"error": "Connexion à la base de données échouée."})


def get_predictions(films):
    url = os.getenv('URL_API') # Ajustez l'URL si nécessaire
    headers = {'Content-Type': 'application/json'}

    # Prépare les données pour l'API
    for film in films:
        #print(film)
        data = {
            'budget': film['budget'] if film['budget'] is not None else 25000000,  # Médiane pour le budget
            'duree': film['duree'] if film['duree'] is not None else 107,  # Médiane pour la durée
            'genre': film['genre'] if film['genre'] is not None else 'missing',
            'pays': film['pays'] if film['pays'] is not None else 'missing',
            'salles_premiere_semaine': film['salles'] if film['salles'] is not None else None,  # Assumez une médiane ou laissez None si géré côté API
            'scoring_acteurs_realisateurs': film['scoring_acteurs_realisateurs'],  # Include the updated scoring
            'coeff_studio': film['coeff_studio'],
            'year': film['date_sortie'].year if film['date_sortie'] and film['date_sortie'].year else None  # Assumez une médiane ou laissez None si géré côté API
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            prediction = response.json()
            film['prediction_entrees'] = int(prediction['prediction']) #stock la prediction
            film['estimation_entrees_cinema'] = int(film['prediction_entrees']/2000)
            film['estimation_entrees_quot'] = int(film['estimation_entrees_cinema']/7)
            film['estimation_recette_hebdo'] = film['estimation_entrees_cinema']*10
            #print(film['scoring_acteurs_realisateurs'])
            #print(film['coeff_studio'])
            #print(f"************************************{film['prediction_entrees']}")
            PredictionFilm.objects.update_or_create(
                titre=film['titre'],
                defaults={'prediction_entrees': film['prediction_entrees']}
            )
        else:
            film['prediction_entrees'] = f'Erreur de prédiction: {response.status_code} - {response.text}'
    return films

@login_required
def chiffre_page(request):
    return render(request, 'main/chiffre_page.html')

@login_required
def archive_page(request):
    return render(request, "main/archive_page.html")


#Lorsque vous configurez une tâche périodique avec Celery, celle-ci est exécutée de manière autonome selon
# l'horaire défini, et non pas à chaque fois que la page est appelée. Cela signifie que la tâche pour récupérer
# les films et obtenir les prédictions se déclenchera automatiquement à l'heure prévue chaque semaine, 
#indépendamment des requêtes des utilisateurs sur votre site web.

#Pour clarifier le fonctionnement :

#Planification de la tâche : La tâche est configurée pour s'exécuter à un moment spécifique 
#(par exemple, tous les lundis à minuit). Cette planification est gérée par Celery Beat, 
#qui surveille l'heure et déclenche l'exécution de la tâche conformément à son calendrier.
#Exécution indépendante : Une fois déclenchée par Celery Beat, la tâche s'exécute de manière indépendante 
#du cycle de vie des requêtes HTTP de votre site web. Elle fonctionne en arrière-plan et n'affecte pas les
# performances ou le fonctionnement de vos vues Django, sauf si vous avez configuré quelque chose pour que les 
#vues interagissent avec les résultats de cette tâche.
#Non-liée aux requêtes des utilisateurs : Les utilisateurs qui accèdent à votre site ne déclenchent pas cette tâche. Ils verront simplement les résultats (par exemple, les films et les prédictions) qui ont été générés et sauvegardés lors de la dernière exécution de la tâche.