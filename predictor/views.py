import joblib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import numpy as np

knn_model = joblib.load('knn_model.pkl')


def home(response):
    return render(response, "features/home.html")

def risk_assessment(response):
    return render(response, "features/risk_assessment.html")

def about(response):
    return render(response, "features/about.html")

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect ("/home")
    else:
       form = UserCreationForm()
       
    return render(response, "registration/register.html", {"form":form})

def login(response):
    return render(response, "registration/login.html")




knn_model = joblib.load('knn_model.pkl')


def prediction_result(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cholesterol = request.POST.get('cholesterol')
        blood_pressure = request.POST.get('blood_pressure')
        heart_rate = request.POST.get('heart_rate')
        smoking = request.POST.get('smoking')
        alcohol_intake = request.POST.get('alcohol')
        exercise_hours = request.POST.get('exercise_hours')
        diabetes = request.POST.get('diabetes')
        family_history = request.POST.get('family_history')
        obesity = request.POST.get('obesity')
        stress_level = request.POST.get('stress_level')
        blood_sugar = request.POST.get('blood_sugar')
        chest_pain_type = request.POST.get('chest_pain_type')
        exercise_induced_angina = request.POST.get('exercise')

        input_data = [[ age, gender, cholesterol, blood_pressure, heart_rate, smoking, alcohol_intake, exercise_hours, diabetes, family_history, obesity, stress_level, blood_sugar, chest_pain_type, exercise_induced_angina]]
        prediction = knn_model.predict(input_data)
        prediction_result = "Heart Disease" if prediction == 1 else "No Heart Disease"
        
    return render(request, 'features/predict.html', {'prediction_result': prediction_result})


# Create your views here.
