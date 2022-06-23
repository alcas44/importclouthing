from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    rol = models.CharField(max_length=250,null=True,blank=True)