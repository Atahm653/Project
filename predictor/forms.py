from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CustomRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput, required=True
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput, required=True
    )
    
    class Meta:
        model= User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
           user.save()
        return user