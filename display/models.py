from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to="profile")


class Write(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    folder_page = models.CharField(max_length=225, null=True, blank=True)
    title = models.CharField(max_length=225)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=4000)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"


class Folder(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    write = models.ForeignKey(Write, default=None, on_delete=models.CASCADE)
    folder = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.user.username}"
