from django.contrib import admin

# Register your models here.

from .models import UserRegistration, Prediction, RiskAssessment

admin.site.register(UserRegistration)
admin.site.register(Prediction)
admin.site.register(RiskAssessment)
