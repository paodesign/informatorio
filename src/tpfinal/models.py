from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    pass
    # nacionalidad =models.CharField(max_length=30)