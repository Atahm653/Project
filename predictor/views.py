import joblib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomRegistrationForm
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def home(request):
    return render(request, "features/home.html")

@login_required
def risk_assessment(request):
    return render(request, "features/risk_assessment.html")

def about(request):
    return render(request, "features/about.html")

def register(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect ("/home")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
       form = CustomRegistrationForm()
       
    return render(request, "registration/register.html", {"form":form})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("/home")
            
        else:
            messages.error(request, "Invalid username or password.")
    

    return render(request, "registration/login.html")


# Load the model from the file
knn_model = joblib.load('models/knn_model.pkl')
scaler = joblib.load('models/scaler.pkl')

print("Scaler type:", type(scaler))
print("KNN model type:", type(knn_model))

print("Scaler mean:", scaler.mean_)  
print("Scaler std:", scaler.scale_)  

@login_required
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

        
        except Exception as e:
            return render(request, 'features/prediction_result.html', {'error': f'An error occurred: {str(e)}'})

    return render(request, 'features/prediction_result.html')

# Create your views here.
