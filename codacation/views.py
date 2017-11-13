from django import http
from django.conf import settings
from django.template.response import TemplateResponse

def context (request):
  return {'DEV': settings.DEBUG}
  
def favicon (request):
  return http.HttpResponseRedirect(settings.STATIC_URL + 'favicon.ico')
  
def home (request):
  return TemplateResponse(request, 'home.html', {})
  