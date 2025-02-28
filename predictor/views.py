import joblib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


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


def prediction_result(response):
    if response.method == 'POST':
        age = response.POST.get('age')
        gender = response.POST.get('gender')
        cholesterol = response.POST.get('cholesterol')
        blood_pressure = response.POST.get('blood_pressure')
        heart_rate = response.POST.get('heart_rate')
        smoking = response.POST.get('smoking')
        alcohol_intake = response.POST.get('alcohol')
        exercise_hours = response.POST.get('exercise_hours')
        diabetes = response.POST.get('diabetes')
        family_history = response.POST.get('family_history')
        obesity = response.POST.get('obesity')
        stress_level = response.POST.get('stress_level')
        blood_sugar = response.POST.get('blood_sugar')
        chest_pain_type = response.POST.get('chest_pain_type')
        exercise_induced_angina = response.POST.get('exercise')

        input_data = [[ age, gender, cholesterol, blood_pressure, heart_rate, smoking, alcohol_intake, exercise_hours, diabetes, family_history, obesity, stress_level, blood_sugar, chest_pain_type, exercise_induced_angina]]
        prediction = knn_model.predict(input_data)
        prediction_result = "Heart Disease" if prediction == 1 else "No Heart Disease"
        
    return render(response, 'features/predict.html', {'prediction_result': prediction_result})


# Create your views here.
