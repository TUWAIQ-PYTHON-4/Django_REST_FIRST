from django.urls import path
from . import views

app_name = "FirstRestApp"

urlpatterns = [
    path("date/", views.date, name="date"),
    path("random/", views.random, name="random"),

]