from rest_framework import serializers

from .models import Information, Category

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ("id","name","address","phone","tagline","email")

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'