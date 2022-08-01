from display.models import Write, Folder
from django import forms
from display.models import Folder


class WriteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"style": "background-color:#2e2f30;border-color:#2e2f30;color:white;", "class": "form-control"}))
    link = forms.URLField(required=False, widget=forms.URLInput(attrs={"style": "background-color:#2e2f30;border-color:#2e2f30;color:white;", "class": "form-control mb-5"}))

    class Meta:
        model = Write

        # will same with models
        widgets = {
            "description": forms.Textarea(attrs={"style": "background-color:#2e2f30;border-color:#2e2f30;color:white;", "class": "form-control mb-3", "rows": 20, "cols": 45}),
            # "link": forms.URLInput(attrs={"style": "background-color:#2e2f30;border-color:#2e2f30;", "class": "form-control mb-3"})
        }
        fields = ["title", "link", "description"]


class FolderForm(forms.ModelForm):
    folder = forms.CharField(widget=forms.TextInput(attrs={"style": "background-color:#2e2f30;border-color:#2e2f30;color:white;", "class": "form-control mb-3"}))
    class Meta:
        model = Folder
        # widgets = {
        #     "folder":forms.TextInput(attrs={"class": "form-control mb-3"})
        # }
        fields = ["folder"]
