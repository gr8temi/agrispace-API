from rest_framework import serializers

from .models import Information

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ("id","name","address","phone","tagline","email")