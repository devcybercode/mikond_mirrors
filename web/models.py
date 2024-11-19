from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class UserModel(AbstractUser):
    pass

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