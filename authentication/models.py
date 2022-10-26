from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    CREATOR = 'CREATOR'
    FARMER = 'FARMER'

    ROLE_CHOICES = (
        (CREATOR, 'Creator'),
        (FARMER, 'Farmer'),
    )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)