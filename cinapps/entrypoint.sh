#!/bin/sh

# while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#   echo "En attente de la disponibilité de Postgres..."
#   sleep 1
# done

# Effectuer les migrations
echo "Effectuer les migrations de la base de données..."

python manage.py makemigrations && python manage.py migrate

python manage.py collectstatic --no-input

echo "Lancer le serveur"

### production ###
# ### Version avec gunicorn pour le serveur web
gunicorn cinapps.wsgi:application --workers=4 --bind=0.0.0.0:8000 --reload


# dev en local ###
# python manage.py runserver 0.0.0.0:8000
