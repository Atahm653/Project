import joblib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import CustomRegistrationForm, CustomLoginForm
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from .models import Prediction 

def home(request):
    return render(request, "features/home.html")

def risk_assessment(request):
    return render(request, "features/risk_assessment.html")

def about(request):
    return render(request, "features/about.html")

def register(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful. You are now registered.")
            return redirect("home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        storage = messages.get_messages(request)
        storage.used = True
    return render(request, "registration/register.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember') == 'on'

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return render(request, "registration/login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.last_login = timezone.now()
            user.save()
            auth_login(request, user)

            if not remember:
                request.session.set_expiry(0)

            messages.success(request, "Login successful!")
            return redirect('risk')
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, "User does not exist.")
            else:
                messages.error(request, "Invalid password.")
            return render(request, "registration/login.html")
    else:
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, "registration/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

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

            # Map prediction result to risk percentage and level
            risk_percentage = 80.0 if prediction[0] == 1 else 20.0
            risk_level = "High" if prediction[0] == 1 else "Low"

            # Save the prediction to the database
            Prediction.objects.create(
                user=request.user,
                risk_percentage=risk_percentage,
                risk_level=risk_level,
                input_data={
                    'age': age,
                    'gender': gender,
                    'cholesterol': cholesterol,
                    'blood_pressure': blood_pressure,
                    'heart_rate': heart_rate,
                    'smoking': smoking,
                    'alcohol_intake': alcohol_intake,
                    'exercise_hours': exercise_hours,
                    'family_history': family_history,
                    'diabetes': diabetes,
                    'obesity': obesity,
                    'stress_level': stress_level,
                    'blood_sugar': blood_sugar,
                    'exercise_induced_angina': exercise_induced_angina,
                    'chest_pain_type': chest_pain_type,
                }
            )

            context = {
                'risk_percentage': risk_percentage,
                'risk_level': risk_level,
                'assessment_date': timezone.now().strftime('%B %d, %Y'),
                'metrics': {
                    'blood_pressure': f"{blood_pressure}/80 mmHg",
                    'cholesterol': f"{cholesterol} mg/dL",
                    'heart_rate': f"{heart_rate} BPM",
                    'blood_sugar': f"{blood_sugar} mg/dL",
                },
                'risk_factors': {
                    'smoking': 'High Impact' if smoking else 'No Impact',
                    'family_history': 'Medium Impact' if family_history else 'No Impact',
                    'stress_level': 'Low Impact' if stress_level < 5 else 'Medium Impact',
                    'exercise': 'No Impact' if exercise_hours > 0 else 'Low Impact',
                },
                'recommendations': [
                    {'title': 'Maintain Regular Exercise', 'description': 'Continue with at least 150 minutes per week.'},
                    {'title': 'Healthy Diet', 'description': 'Focus on fruits, vegetables, whole grains, and lean proteins.'},
                    {'title': 'Quit Smoking', 'description': 'Consider smoking cessation programs.'} if smoking else None,
                    {'title': 'Regular Check-ups', 'description': 'Schedule annual check-ups.'},
                ]
            }
            context['recommendations'] = [r for r in context['recommendations'] if r]
            return render(request, 'features/prediction_result.html', context)

        except Exception as e:
            return render(request, 'features/prediction_result.html', {'error': f'An error occurred: {str(e)}'})

    return render(request, 'features/prediction_result.html')