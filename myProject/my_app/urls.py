from django.urls import path
from . import views

urlpatterns = [
    path("today", views.get_today_date, name="date_today"),
    path("random", views.random_number, name="random")
]