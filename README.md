### Projet Cinéma "New is Always Better"

Le cinéma "New is Always Better" souhaite développer un outil décisionnel pour optimiser la sélection des films à projeter. Actuellement, le gérant s'appuie sur son intuition et son expérience, combinées à une veille sur les nouveautés et sa participation à des festivals. Cependant, cette approche chronophage nécessite une automatisation partielle pour optimiser la gestion des projections.
Politique de Diffusion
Le cinéma ne diffuse que les nouveautés lors de leur première semaine, renouvelant la programmation chaque mercredi dans ses deux salles, l'une pour 120 spectateurs et l'autre pour 80.

#### Objectifs

L'objectif est d'utiliser l'intelligence artificielle pour estimer la fréquentation des nouveaux films dès leur sortie, afin d'optimiser la programmation et maximiser les revenus. L'outil sera accessible via une application web ou mobile conviviale, sans nécessiter de compétences techniques avancées.

Logique Métier:

    Estimation du Potentiel des Films: Estimation du nombre d'entrées nationales pour chaque film et calcul du potentiel d'audience du cinéma.
    Sélection et Programmation: Allocation des films aux salles en fonction de leur potentiel estimé.
    Calcul de la Recette et de l'Audience Quotidienne: Projection des recettes et de l'audience estimée pour chaque film.
    Gestion des Coûts: Soustraction des coûts fixes pour évaluer la rentabilité de la semaine.


L'équipe de développement IA, composée de 4 développeurs, devra :

    Se familiariser avec l'industrie du cinéma.
    Créer un algorithme de régression pour prédire le nombre d'entrées des films.
    Constituer un jeu de données d'entraînement en utilisant le scraping.
    Mettre en œuvre MLflow pour gérer les expériences de machine learning.
    Automatiser le scraping et les prédictions.
    Développer une application web Django pour afficher les informations pertinentes.
    Utiliser une architecture de micro-services avec FastAPI, Django et une BDD transactionnelle et analytique.
    Synchroniser Jira et GitHub pour la méthodologie agile.

Enjeux Majeurs

La gestion de projet agile et la collaboration efficace entre les membres de l'équipe sont des enjeux clés pour la réussite de ce projet.

Ressources Techniques

    Machine Learning
    Django
    FastAPI
    Docker
    Azure
    Scrapy
    Cron
    Jira
    MLflow

Le projet sera réalisé en 4 sprints, avec une présentation finale de l'outil au client à la fin du quatrième sprint.
