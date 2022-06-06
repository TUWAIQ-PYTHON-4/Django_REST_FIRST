from django.urls import path
from . import views

urlpatterns = [
    path('date/', views.Date, name='date'),
    path('random/', views.Random, name='random'),

]