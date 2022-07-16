from display.models import Write, Folder
from django import forms
from display.models import Folder


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ["title", "link", "description"]


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["folder"]
