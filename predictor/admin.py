from django.contrib import admin

# Register your models here.

from .models import Patient
from .models import Prediction
from .models import RiskAssessment

admin.site.register(Patient)
admin.site.register(Prediction)
admin.site.register(RiskAssessment)
