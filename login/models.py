from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('normal', 'Normal'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='normal')
    objects = CustomUserManager()

    def __str__(self):
        return self.username
