import joblib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


# Load the model from the file
knn_model = joblib.load('knn_model.pkl')
scaler = joblib.load('scaler.pkl')



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

def prediction_result(request):
    if request.method == 'POST':
      try:
        age = float(request.POST.get('age'))
        gender = float(request.POST.get('gender'))
        cholesterol = float(request.POST.get('cholesterol'))
        blood_pressure = float(request.POST.get('blood_pressure'))
        heart_rate = float(request.POST.get('heart_rate'))
        smoking = float(request.POST.get('smoking'))
        alcohol_intake = float(request.POST.get('alcohol_intake'))
        exercise_hours = float(request.POST.get('exercise_hours'))
        family_history = float(request.POST.get('family_history'))
        diabetes = float(request.POST.get('diabetes'))
        obesity = float(request.POST.get('obesity'))
        stress_level = float(request.POST.get('stress_level'))
        blood_sugar = float(request.POST.get('blood_sugar'))
        exercise_induced_angina = float(request.POST.get('exercise_induced_angina'))
        chest_pain_type = float(request.POST.get('chest_pain_type'))

      except ValueError:
            print("Invalid Input")
        

    input_data =np.array([[ age, gender, cholesterol, blood_pressure, heart_rate, smoking, alcohol_intake, exercise_hours, family_history, diabetes, obesity, stress_level, blood_sugar,  exercise_induced_angina, chest_pain_type]])
    input_data = scaler.transform(input_data)

    prediction = knn_model.predict(input_data)
    prediction_result = "Heart Disease" if prediction == 1 else "No Heart Disease"
        
    return render(request, 'features/predict.html', {'prediction_result': prediction_result})


# Create your views here.
