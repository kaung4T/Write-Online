from django.urls import path, include
from display import views

urlpatterns = [
    path("", views.home, name="index"),
]