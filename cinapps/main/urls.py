from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('chiffre/', views.chiffre_page, name='chiffre'),
    path('archive/', views.archive_page, name='archive'),
    path('prediction/', views.get_films, name='prediction'),
]