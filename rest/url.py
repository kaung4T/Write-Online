from django.urls import path, include
from rest import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api", views.get_api),

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