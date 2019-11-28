from rest_framework import serializers

from .models import Information, Category

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ("id","name","address","phone","tagline","email")

class CategorySerializers(serializers.ModelSerializer):
    """
    This serializer serializes Category model
    attribute:
         model(class) - Model to be serialized
    """
    class Meta:
        """
        states fields from class to be serialized
        attributes:
            category_name(string)- the name of the job category
            description(string)- the description of the category
            image(string)- the image to represent the category
        """
        model = Category
        fields = '__all__'