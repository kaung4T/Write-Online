from display.models import Write, Folder
from django import forms
from display.models import Folder


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        widgets = {
            "description": forms.Textarea(attrs={"style": "background-color:#2e2f30;border-color:#2e2f30;", "class": "form-control", "rows": 20, "cols": 45}),
        }
        fields = ["title", "link", "description"]


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["folder"]
