from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("risk", views.risk_assessment, name="risk"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
]