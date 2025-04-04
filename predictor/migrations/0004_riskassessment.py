# Generated by Django 5.1.6 on 2025-02-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0003_prediction'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('cholesterol', models.IntegerField(max_length=3, null=True)),
                ('blood_pressure', models.IntegerField(max_length=3, null=True)),
                ('heart_rate', models.IntegerField(max_length=3, null=True)),
                ('smoking', models.CharField(max_length=10, null=True)),
                ('alcohol', models.CharField(max_length=10, null=True)),
                ('diabetes', models.CharField(max_length=10, null=True)),
                ('family_history', models.CharField(max_length=10, null=True)),
                ('obesity', models.CharField(max_length=10, null=True)),
                ('stress', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
