from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, PredApi, PredictionFilm

admin.site.register(User, UserAdmin)

#enregistrement en bdd des données de prédiction
admin.site.register(PredApi)

#enregistrement en bdd des données de prédiction des films
admin.site.register(PredictionFilm)
