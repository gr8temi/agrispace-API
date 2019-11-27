from django.db import models

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
