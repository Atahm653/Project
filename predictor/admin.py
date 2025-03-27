from django.contrib import admin

# Register your models here.

from .models import UserProfile, Prediction, RiskAssessment

admin.site.register(UserProfile)
admin.site.register(Prediction)
admin.site.register(RiskAssessment)
