from django.shortcuts import render
from .functions import multiplicate_by_5
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
import json
import mysql.connector
from .database import connect_to_azure_mysql
import requests
from datetime import datetime, timedelta
import pandas as pd

@login_required
def home_page(request):
    conn = connect_to_azure_mysql()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            date_semaine = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            query = "SELECT titre, description, image, date_sortie, genre, salles, pays, studio, duree, budget FROM films WHERE date_sortie >= %s" #scoring
            cursor.execute(query, (date_semaine,))
            films = cursor.fetchall()

            #boucle de pred pour chaque film 
            predictions_films = []
            for film in films:
                prediction = get_predictions(film)
                predictions_films.append((prediction, film))
                film['prediction_entrees'] = prediction

            cursor.close()
            conn.close()

            ## Trie films par préd d'entrées dans l'ordre décroissant
            predictions_films_sorted = sorted(predictions_films, key=lambda x: x[0]['prediction'], reverse=True)
            films_sorted = [film for prediction, film in predictions_films_sorted]
            
            return render(request, "main/home_page.html", {"films": films_sorted})
        

        except mysql.connector.Error as e:
            print(f"Erreur lors de l'exécution de la requête SQL: {e}")
            return render(request, 'main/home_page.html', {"error": str(e)})
    else:
        print("La connexion à la base de données n'a pas été établie avec succès.")
        return render(request, 'main/home_page.html', {"error": "Connexion à la base de données échouée."})

def get_studio_coefficient(studio):
    conn = connect_to_azure_mysql()
    if conn:
        try:
            cursor = conn.cursor()
            
            query = """
                SELECT
                    CASE
                        WHEN studio IN ('Walt Disney Pictures','Warner Bros.','Paramount','Sony Pictures','Universal','20th Century Fox','Lionsgate','Columbia') THEN 3
                        WHEN studio IN ('Pathé','Studiocanal','Gaumont','UGC Distribution','SND','Le Pacte','Metropolitan','EuropaCorp','GBVI','Wild Bunch','UFD','ARP Selection','Ad vitam','Haut et Court','Films du Losange','Rezo Films','TFM Distribution') THEN 2
                        WHEN studio IN ('Gébéka','Memento Films','KMBO','Océan Films','AMLF','MK2 Diffusion','Gaumont Sony','Apollo Films','Sophie Dulac','Eurozoom','Jour2Fête','Pan-Européenne','Cinema Public','Polygram') THEN 1
                        ELSE 0
                    END AS studio_coefficient
                FROM
                    films
                WHERE
                    studio = %s
            """
            cursor.execute(query, (studio,))
            studio_coef = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return studio_coef
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'exécution de la requête SQL: {e}")
            return None
    else:
        print("La connexion à la base de données n'a pas été établie avec succès.")
        return None
    
def scoring_casting(film):
    conn = connect_to_azure_mysql()
    cursor = conn.cursor()

    query = """SELECT f.id_film, GROUP_CONCAT(p2.nom) AS noms
        FROM films f
        LEFT JOIN participations p ON f.id_film = p.id_film 
        JOIN personnes p2 ON p.id_personne = p2.id_personne 
        GROUP BY f.id_film""" #recuperer les noms des personnes dans une liste

    cursor.execute(query)
    resultats = cursor.fetchall()

    #charger le csv
    actors = pd.read_csv('main/acteurs_coef.csv')

    poids_total = 0
    for resultat in resultats: 
        noms_personnes_dans_film = resultat[1].split(',') #transformer le tuple en liste
        for personne in noms_personnes_dans_film:
            if personne in actors['name'].values:
                poids_acteur = actors.loc[actors['name'] == personne, 'coef_personne'].values[0]  # Récupérer le poids de l'acteur dans le dataframe 'actors'
                poids_total += poids_acteur  # Multiplie le poids de l'acteur par la valeur présente dans poids_total
        names = actors['name'].values

    conn.close()

    return poids_total 


def get_predictions(film):
    url = os.getenv('URL_API') # Ajustez l'URL si nécessaire
    headers = {'Content-Type': 'application/json'}
    print('****TYPE DE FILMet contenu de FILM',type(film), film)
    #film = json.loads(film)
    payload= {
        'budget': film['budget'],
        'duree': film['duree'],
        'genre': film['genre'],
        'pays': film['pays'],
        'salles_premiere_semaine': film['salles'],
        'scoring_acteurs_realisateurs': scoring_casting(film),#calculé avec fonction scoring_casting qui requete tables film, participe et personnes,
        'coeff_studio': get_studio_coefficient(film['studio']),
        'year': film['date_sortie'].year}
    print('**************', type(payload), payload) #payload est un dico ici

    for key, value in payload.items(): #gestion des None qui empechent l'api de faire pred
        print ('########', payload[key])
        if payload[key] == None:
            payload[key] = 0
        print('%%%%%%%%%%', payload)



    response = requests.post(url, json=payload)
    if response.status_code == 200:
        prediction = response.json()
        print('Prediction:', prediction)
        return prediction
    else:
        print(f"Echec de la requete à l'api: {response.status_code}")
        return None

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