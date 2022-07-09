from django.urls import path, include
from rest import views

urlpatterns = [
    # Test in POSTman
    path("rest", views.Resting.as_view(), name="rest"),
    path("rest/<str:pk>", views.Resting.as_view(), name="rest"),
    path("rest/<str:pk>", views.Resting.as_view(), name="rest"),

    path("api-auth", include("rest_framework.urls")),
]