from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Assurez-vous que l'URL de login est configurée.
    template_name = 'registration/signup.html'