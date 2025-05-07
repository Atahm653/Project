from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    risk_percentage = models.FloatField(default=0.0)
    risk_level = models.CharField(max_length=20, default="unknown")
    assessment_date = models.DateTimeField(auto_now_add=True)
    input_data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username} - {self.risk_level} Risk on {self.assessment_date.strftime('%B %d, %Y')}"