from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("today/", views.today, name="today"),
    path("random/", views.random, name="random")

]