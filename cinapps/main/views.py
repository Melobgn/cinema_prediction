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

@login_required
def home_page(request):
    # Connexion à la base de données MySQL Azure
    conn = connect_to_azure_mysql()
    
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT titre, description, image, date_sortie, genre, salles, entrees, entrees_pred FROM films order by date_sortie DESC")
            films = cursor.fetchall()
            cursor.close()
            conn.close()
            
            # Traitez les données récupérées comme vous le souhaitez
            # Par exemple, renvoyez les films à votre modèle
            return render(request, "main/home_page.html", {"films": films})
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'exécution de la requête SQL: {e}")
    else:
        print("La connexion à la base de données n'a pas été établie avec succès.")
        # Gérez cette erreur en conséquence dans votre vue

    return render(request, 'main/home_page.html')

@login_required
def chiffre_page(request):
    return render(request, 'main/chiffre_page.html')

@login_required
def archive_page(request):
    # Connexion à la base de données MySQL Azure
    conn = connect_to_azure_mysql()
    
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT titre, description, image, date_sortie, genre, salles, entrees, entrees_pred FROM films order by date_sortie DESC")
            films = cursor.fetchall()
            cursor.close()
            conn.close()
            
            # Traitez les données récupérées comme vous le souhaitez
            # Par exemple, renvoyez les films à votre modèle
            return render(request, "main/archive_page.html", {"films": films})
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'exécution de la requête SQL: {e}")
    else:
        print("La connexion à la base de données n'a pas été établie avec succès.")
        # Gérez cette erreur en conséquence dans votre vue

    return render(request, "main/archive_page.html")
