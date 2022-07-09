from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to="profile")


class Write(models.Model):
    title = models.CharField(max_length=225)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=4000)
    time = models.TimeField(auto_now_add=True)