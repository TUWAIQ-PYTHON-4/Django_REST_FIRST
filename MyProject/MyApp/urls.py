from django.urls import path
from . import views


app_name = "random"

urlpatterns = [
  
  path("index/", views.index, name= "index"),
  path("random/", views.random, name= "random"),

]