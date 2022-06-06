from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("index/", views.get_date, name="index"),
    path("rand/", views.rando, name="rand"),

]