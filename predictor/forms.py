from django import forms
from .models import UserRegistration
from django.contrib.auth.hashers import make_password

class CustomRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password', 'password2']
