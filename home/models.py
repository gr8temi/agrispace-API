from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import cloudinary
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Create your models here.
class Information(models.Model):
    """Model definition for Information."""

    # TODO: Define fields here
    name =  models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField( max_length=50)
    tagline = models.TextField()
    email = models.EmailField(max_length=256)

    class Meta:
        """Meta definition for Information."""

        verbose_name = 'Information'
        verbose_name_plural = 'Informations'

    def __str__(self):
        """Unicode representation of Information."""
        return self.name

class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    category_name = models.CharField( max_length=50)
    description  = RichTextField()
    image = CloudinaryField('image')
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.category_name

@receiver(pre_delete, sender=Category)

def photo_delete(sender, instance, **kwargs):
    """
    Deletes image associated to the instance of the category
    """
    cloudinary.uploader.destroy(instance.image.public_id)
