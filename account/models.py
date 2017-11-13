from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
  version = models.PositiveIntegerField(default=1)
  