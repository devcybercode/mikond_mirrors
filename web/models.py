from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class UserModel(AbstractUser):
    pass

class SocialContact(models.Model):
    instagram = models.URLField()
    telegram = models.URLField()
    phone_number = models.CharField(
        max_length=15,  # Adjust based on your region's phone number format
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',  # Validates international phone numbers
                message=(
                    "Phone number must be entered in the format: '+9981234567'. "
                    "Up to 15 digits allowed."
                ),
            )
        ],
    )

    class Meta:
        verbose_name = 'Social Contact'
        verbose_name_plural = 'Social Contacts'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.instagram}, {self.telegram}"

class mirrors(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='mirrors/%Y/%m/%d/')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mirror'
        verbose_name_plural = 'Mirrors'
        ordering = ('-id',)