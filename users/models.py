from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = models.TextField(null=True)
    email = models.EmailField(_('email address'), unique=True)
    exp_level = models.IntegerField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    #TODO: spouse_name = models.CharField(blank=True, max_length=100)
    #date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.email
