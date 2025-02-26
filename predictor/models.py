from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(max_length=3, null=True)
    gender = models.CharField(max_length=10, null=True)
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
    
class RiskAssessment(models.Model):
    age = models.IntegerField(max_length=3, null=True)
    gender = models.CharField(max_length=10, null=True)
    cholesterol = models.IntegerField(max_length=3, null=True)
    blood_pressure = models.IntegerField(max_length=3, null=True)
    heart_rate = models.IntegerField(max_length=3, null=True)
    smoking = models.CharField(max_length=10, null=True)
    alcohol = models.CharField(max_length=10, null=True)
    diabetes = models.CharField(max_length=10, null=True)
    family_history = models.CharField(max_length=10, null=True)
    obesity = models.CharField(max_length=10, null=True)
    stress = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.result

