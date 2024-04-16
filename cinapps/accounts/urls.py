from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    # Autres URL si nécessaire
]
