from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response, "accounts/home.html")

def risk_assessment(response):
    return render(response, "accounts/risk_assessment.html")

# Create your views here.
