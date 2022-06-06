from django.urls import path
from . import views

app_name = 'testApp'
urlpatterns = [
    path("date/", views.date, name="date"),
    path("random_number/", views.random_number, name="random_number"),
]
