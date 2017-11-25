from django.contrib import admin

from classroom.models import Klass

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
  list_display = ('name', 'created', 'invite_code', 'Admins')
  list_filter = ('created',)
  search_fields = ('name', 'admins__email')
  
  raw_id_fields = ('admins', 'students')
  
  def Admins (self, obj):
    return ', '.join(obj.admins.all().values_list('email', flat=True))
    