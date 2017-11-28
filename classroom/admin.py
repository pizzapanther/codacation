from django.contrib import admin

from classroom.models import Klass, Assignment, Issue

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
  list_display = ('name', 'created', 'invite_code', 'Admins')
  list_filter = ('created',)
  search_fields = ('name', 'admins__email')
  
  raw_id_fields = ('admins', 'students')
  
  def Admins (self, obj):
    return ', '.join(obj.admins.all().values_list('email', flat=True))
    
class IssueInline (admin.StackedInline):
  model = Issue
  raw_id_fields = ('student',)
  
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
  list_display = ('name', 'created', 'klass')
  list_filter = ('created',)
  search_fields = ('name', 'repo_url')
  
  raw_id_fields = ('klass',)
  
  inlines = [IssueInline]