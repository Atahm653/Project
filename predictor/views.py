from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def home(response):
    return render(response, "features/home.html")

def risk_assessment(response):
    return render(response, "features/risk_assessment.html")

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect ("/home")
    else:
       form = UserCreationForm()
       
    return render(response, "registration/register.html", {"form":form})

# Create your views here.
