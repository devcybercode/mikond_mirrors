from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class UserModel(AbstractUser):
    pass

class SocialContact(models.Model):
    instagram = models.URLField()
    telegram = models.URLField()
    logo = models.ImageField(upload_to='logo/%Y/%m/%d/', default="none")
    phone_number = models.CharField(
        max_length=15,  
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',  
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
        
phone_validator = RegexValidator(
    regex=r'^\+998 \(\d{2}\) \d{3} \d{2} \d{2}$',
    message="Номер должен быть в формате: +998 (__) ___ __ __"
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=20,
        validators=[phone_validator],
        help_text="Формат номера: +998 (__) ___ __ __"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
