from django.urls import path
from . import views


urlpatterns = [
path("date/", views.get_date, name="get_date"),
path("random/", views.add_random, name="add_random"),
    ]