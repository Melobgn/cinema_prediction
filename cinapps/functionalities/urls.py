from django.urls import path
from functionalities import views

urlpatterns = [
    path('list/', views.FunctionalitiesListView.as_view(), name="func-list"),
    path('<int:pk>/', views.FunctionalitiesDetailView.as_view(), name="func-detail"),
  
]