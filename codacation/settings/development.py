# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from codacation.settings.base import *

try:
  from codacation.settings.local import *
  
except ImportError:
  pass

else:
  print('Loaded local.py settings')
  