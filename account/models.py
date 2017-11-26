from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
  version = models.PositiveIntegerField(default=1)
  
  @property
  def name (self):
    if self.first_name and self.last_name:
      return '{} {}'.format(self.first_name, self.last_name)
      
    elif self.first_name:
      return self.first_name
      
    elif self.last_name:
      return self.last_name
      
    return self.email
    