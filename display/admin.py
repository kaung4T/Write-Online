from django.contrib import admin
from display.models import UserProfile, Write
from display.models import Write, Folder
from display.models import Folder
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["image"]


class WriteAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "time"]


class FolderAdmin(admin.ModelAdmin):
    list_display = ["user", "write", "folder"]


admin.site.register(UserProfile)
admin.site.register(Write, WriteAdmin)
admin.site.register(Folder, FolderAdmin)
