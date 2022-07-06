from django.contrib import admin
from display.models import UserProfile

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["image"]

admin.site.register(UserProfile)