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
