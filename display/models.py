from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to="profile")