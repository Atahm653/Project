from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    risk_percentage = models.FloatField()
    risk_level = models.CharField(max_length=20)
    assessment_date = models.DateTimeField(auto_now_add=True)
    input_data = models.JSONField()

    def __str__(self):
        return f"{self.user.username} - {self.risk_level} Risk on {self.assessment_date.strftime('%B %d, %Y')}"