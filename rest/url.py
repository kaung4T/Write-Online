from django.urls import path, include
from rest import views

urlpatterns = [
    # Test in POSTman
    path("rest", views.Resting.as_view(), name="rest"),
    path("rest/<str:pk>", views.Resting.as_view(), name="put"),
    path("rest/<str:pk>", views.Resting.as_view(), name="del"),

    path("defaultRest", views.display, name="display"),
    path("defaultRest/upload", views.upload, name="upload"),
    path("defaultRest/update/<str:pk>", views.update, name="update"),
    path("defaultRest/delete/<str:pk>", views.delete, name="delete"),

    path("api-auth", include("rest_framework.urls")),
]