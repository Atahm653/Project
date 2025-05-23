from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class CustomRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}), 
        required=True
    )
    password2 = forms.CharField(
        label="Confirm Password", 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}), 
        required=True
    )
    #terms_agreement = forms.BooleanField(
     #   label="I agree to the Terms of Service and Privacy Policy",
      #  required=True,
       # error_messages={'required': 'You must agree to the Terms of Service and Privacy Policy to register.'}
    #)
    
    class Meta:
        model= User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
           user.save()
        return user

# login form
class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        required=True
    )
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        label="Remember me"
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid username or password.")
            elif not self.user.is_active:
                raise forms.ValidationError("This account is inactive.")
        
        return cleaned_data

    def get_user(self):
        return self.user if hasattr(self, 'user') else None