# Utiliser l'image officielle de Python comme base
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de dépendances Python
COPY requirements.txt ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet dans le répertoire de travail du conteneur
COPY . .

# Rendre le script shell exécutable
RUN chmod +x start_spider.sh

# Installer cron
RUN apt-get update && apt-get install -y cron

# Ajouter le fichier crontab au répertoire approprié et donner les permissions adéquates
COPY crontab /etc/cron.d/scrapy-cron
RUN chmod 0644 /etc/cron.d/scrapy-cron

# Appliquer le fichier crontab
RUN crontab /etc/cron.d/scrapy-cron

# Créer un fichier log pour enregistrer les sorties du cron (facultatif)
RUN touch /var/log/cron.log

# Lancer cron en arrière-plan comme processus principal du conteneur
CMD ["cron", "-f"]
