import os

from django import http
from django.conf import settings
from django.template.response import TemplateResponse

from codacation.release import RELEASE

def tpl_files ():
  tpls = []
  
  base_dir = os.path.join(settings.BASE_DIR, 'static', 'coda')
  for root, dirs, files in os.walk(base_dir):
    for file in files:
      if file.endswith('.html'):
        fullpath = os.path.join(root, file)
        relpath = fullpath.replace(base_dir + '/', '')
        relpath = relpath.replace('/', '-')
        relpath = relpath[:-5]
        with open(fullpath, 'r') as fh:
          tpls.append({'path': relpath, 'content': fh.read()})
          
  return tpls
  
def site_context (context):
  context['site'] = {
    'name': 'Codacation',
  }
  
  context['debug'] = settings.DEBUG
  context['release'] = RELEASE
  context['templates'] = tpl_files()
  
  return context
  
def favicon (request):
  return http.HttpResponseRedirect(settings.STATIC_URL + 'favicon.ico')
  
def frontend (request):
  return TemplateResponse(request, 'base.html', site_context({}))
  