from django.urls import path
from . import views

app_name = "RestApp"

urlpatterns = [
    path("date/", views.date, name="date"),
    path("ran/", views.random_num, name="random_num")
]