from django.conf import settings
from django.db import models

class Klass (models.Model):
  name = models.CharField(max_length=75)
  
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  
  admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='admin_classes', blank=True)
  students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='student_classes', blank=True)
  
  invite_code = models.CharField(max_length=255, unique=True)
  
  class Meta:
    ordering = ('-created',)
    verbose_name = 'Class'
    verbose_name_plural = 'Classes'
    
  def __str__ (self):
    return self.name
    
  def is_admin (self, user):
    if user.is_authenticated():
      if self.admins.filter(id=user.id).count() > 0:
        return True
        
    return False
    
class Assignment (models.Model):
  name = models.CharField(max_length=75)
  short_description = models.CharField(max_length=255, blank=True, null=True)
  
  repo_url = models.CharField(max_length=255)
  
  klass = models.ForeignKey(Klass)
  
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  
  def __str__ (self):
    return self.name
    
  class Meta:
    ordering = ('-created',)
    
class Issue (models.Model):
  num = models.IntegerField()
  merge_branch = models.CharField(max_length=255)
  
  assignment = models.ForeignKey(Assignment)
  student = models.ForeignKey(settings.AUTH_USER_MODEL)
  
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  
  def __str__ (self):
    return '#{} - {}'.format(self.num, self.merge_branch)
    