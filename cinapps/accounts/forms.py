from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    #custom
    birth_date = forms.DateField(required=False, help_text='Optional. Format: YYYY-MM-DD')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'birth_date',
                  )