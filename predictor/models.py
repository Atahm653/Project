from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Prediction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    result = models.CharField(max_length=100)
    date_predicted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result
    
sex = (
    (0, 'female'),
    (1, 'male')
)

smoking = (
    (0, 'no'),
    (1, 'yes')
)

alcohol_intake = (
    (0, 'no'),
    (1, 'yes')
)

family_history = (
    (0, 'no'),
    (1, 'yes')
)

diabetes = (
    (0, 'no'),
    (1, 'yes')
)

obesity = (
    (0, 'no'),
    (1, 'yes')
)
    
class RiskAssessment(models.Model):
    age = models.IntegerField(null=True)
    gender = models.PositiveIntegerField(choices=sex, null=True)
    cholesterol = models.IntegerField(null=True)
    blood_pressure = models.IntegerField(null=True)
    heart_rate = models.IntegerField(null=True)
    smoking = models.PositiveIntegerField(null=True)
    alcohol_intake = models.PositiveIntegerField(null=True)
    diabetes = models.PositiveIntegerField(null=True)
    family_history = models.PositiveIntegerField(null=True)
    obesity = models.PositiveIntegerField(null=True)
    stress_level = models.CharField(max_length=10, null=True)
    blood_sugar = models.CharField(max_length=10, null=True)
    exercise_induced_angina = models.CharField(max_length=10, null=True)
    chest_pain_type = models.CharField(max_length=10, null=True)



    def __str__(self):
        return self.result

