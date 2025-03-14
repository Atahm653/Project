from django.db import models

# Create your models here.

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

exercise_induced_angina = (
    (0, 'no'),
    (1, 'yes')
)

chest_pain_type = (
    (0, 'none'),
    (1, 'non-anginal pain'),
    (2, 'atypical angina'),
    (3, 'typical angina')
)


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
    

    
class RiskAssessment(models.Model):
    age = models.IntegerField(null=True)
    gender = models.PositiveIntegerField(choices=sex, null=True)
    cholesterol = models.IntegerField(null=True)
    blood_pressure = models.IntegerField(null=True)
    heart_rate = models.IntegerField(null=True)
    smoking = models.PositiveIntegerField(choices=smoking, null=True)
    alcohol_intake = models.PositiveIntegerField(choices=alcohol_intake, null=True)
    exercise_hours = models.IntegerField(null=True)
    family_history = models.PositiveIntegerField(choices=family_history, null=True)
    diabetes = models.PositiveIntegerField(choices=diabetes, null=True)
    obesity = models.PositiveIntegerField(choices=obesity, null=True)
    stress_level = models.PositiveIntegerField(null=True)
    blood_sugar = models.IntegerField(null=True)
    exercise_induced_angina = models.IntegerField(choices=exercise_induced_angina, null=True)
    chest_pain_type = models.IntegerField(choices=chest_pain_type, null=True)



    def __str__(self):
        return self.result

