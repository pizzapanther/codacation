from django.conf import settings
from django.db import models

class Klass (models.Model):
  name = models.CharField(max_length=75)
  
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  
  admins = models.ManyToManyField(settings.AUTH_USER_MODEL)
  
  invite_code = models.CharField(max_length=255, unique=True)
  
  class Meta:
    ordering = ('-created',)
    verbose_name = 'Class'
    verbose_name_plural = 'Classes'
    
  def __str__ (self):
    return self.name