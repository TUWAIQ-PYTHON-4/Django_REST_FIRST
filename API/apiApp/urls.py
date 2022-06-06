from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('max_min/', views.max_min, name='max_min'),
]
