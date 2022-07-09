from rest_framework import serializers
from display.models import Write

class WriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Write
        fields = ["title", "description"]


