from . import views
from django.urls import path

urlpatterns = [
    path("MyApp/date/", views.date),
    path("MyApp/random/", views.randomview),

]