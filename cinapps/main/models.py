from django.contrib.auth.models import AbstractUser
from django.db import models

# Ceci est un modèle utilisateur personnalisé qui hérite actuellement de AbstractUser.
# Il est prêt à être étendu avec des champs et méthodes supplémentaires si besoin.(comme birth_date ici)
# Si aucun champ supplémentaire n'est requis au-delà du modèle par défaut de Django,
# cette classe peut rester vide et AbstractUser sera utilisé comme tel. 
class User(AbstractUser):
    birth_date = models.DateField(auto_now=False, null=True)
    

#stocker les informations de l'api en bdd
class PredApi(models.Model):
    titre = models.CharField(max_length=100)
    #image = models.ImageField() 
    prediction = models.FloatField()          
    date = models.DateField()

    def __str__(self):
        return self.titre
    pass