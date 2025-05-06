from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("risk", views.risk_assessment, name="risk"),
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("predict", views.prediction_result, name="predict"),
    path('history/', views.history, name='history'),
]