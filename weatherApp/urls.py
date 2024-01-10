from django.urls import path
from . import views

app_name = "weatherApp"
urlpatterns = [
    path("", views.weather, name="weather"),
]