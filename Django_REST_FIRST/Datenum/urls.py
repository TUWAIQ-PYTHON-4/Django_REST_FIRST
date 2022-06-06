from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("", views.mydate, name="mydate"),
    path("random/", views.get_random, name="random")
]


