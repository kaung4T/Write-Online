from django.contrib import admin
from display.models import UserProfile, Write
from display.models import Write

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["image"]

class UserWrite(admin.ModelAdmin):
    list_display = ["title", "description", "time"]

admin.site.register(UserProfile)
admin.site.register(Write, UserWrite)