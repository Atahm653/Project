from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'risk_percentage', 'risk_level', 'assessment_date')
    list_filter = ('risk_level', 'assessment_date')
    search_fields = ('user__username', 'risk_level')