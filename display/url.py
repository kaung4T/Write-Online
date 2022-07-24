from django.urls import path, include
from display import views

urlpatterns = [
    path("", views.home, name="index"),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("folder", views.folder, name="folder"),
    path("write", views.write, name="write"),
    path("write2/<str:pk>", views.write2, name="write2"),
    path("profile", views.profile, name="profile"),
    path("profile2/<str:pk>", views.profile2, name="profile2"),
]
