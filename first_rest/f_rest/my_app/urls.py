from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path("today", views.today, name="today"),
    path("random/", views.random_number, name="random_number")
]