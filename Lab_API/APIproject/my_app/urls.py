from django.urls import path
from . import views

app_name = "my_app"

urlpatterns = [
    path("date/", views.date_today, name="date"),
    path("random/", views.randome_number , name="random")
]