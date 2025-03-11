import joblib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


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


# Load the model from the file
knn_model = joblib.load('models/knn_model.pkl')
scaler = joblib.load('models/scaler.pkl')

def prediction_result(request):
    if request.method == 'POST':
        try:
            age = float(request.POST.get('age', 0))
            gender = float(request.POST.get('gender', 0))
            cholesterol = float(request.POST.get('cholesterol', 0))
            blood_pressure = float(request.POST.get('blood_pressure', 0))
            heart_rate = float(request.POST.get('heart_rate', 0))
            smoking = float(request.POST.get('smoking', 0))
            alcohol_intake = float(request.POST.get('alcohol_intake', 0))
            exercise_hours = float(request.POST.get('exercise_hours', 0))
            family_history = float(request.POST.get('family_history', 0))
            diabetes = float(request.POST.get('diabetes', 0))
            obesity = float(request.POST.get('obesity', 0))
            stress_level = float(request.POST.get('stress_level', 0))
            blood_sugar = float(request.POST.get('blood_sugar', 0))
            exercise_induced_angina = float(request.POST.get('exercise_induced_angina', 0))
            chest_pain_type = float(request.POST.get('chest_pain_type', 0))

           
            input_data = np.array([[age, gender, cholesterol, blood_pressure, heart_rate, smoking, 
                                   alcohol_intake, exercise_hours, family_history, diabetes, obesity, 
                                   stress_level, blood_sugar, exercise_induced_angina, chest_pain_type]])

            input_data_scaled = scaler.transform(input_data)

            prediction = knn_model.predict(input_data_scaled)
            prediction_result = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"

            return render(request, 'features/prediction_result.html', {'prediction_result': prediction_result})

        except ValueError:
            return render(request, 'features/prediction_result.html', {'error': 'Invalid input: Please enter numeric values'})
        except Exception as e:
            return render(request, 'features/prediction_result.html', {'error': f'An error occurred: {str(e)}'})

    return render(request, 'features/prediction_result.html')

# Create your views here.
