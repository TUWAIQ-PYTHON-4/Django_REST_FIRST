from django.urls import path
from . import views

urlpatterns = [
    path("date/", views.date, name="date"),
    path("random/", views.random, name="random")
]