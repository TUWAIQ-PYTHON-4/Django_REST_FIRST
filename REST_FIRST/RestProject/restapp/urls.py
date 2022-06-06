from django.urls import path
from . import views

app_name = "restapp"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("random/", views.random_number, name="random_number"),




]