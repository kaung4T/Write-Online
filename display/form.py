from display.models import Write
from django import forms


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ["title", "link", "description"]
