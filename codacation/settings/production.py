# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

import os

from codacation.settings.base import *
from codacation.release import RELEASE

INSTALLED_APPS.append('raven.contrib.django.raven_compat')

RAVEN_CONFIG = {
  'dsn': os.environ.get('RAVEN_DSN', ''),
  'release': RELEASE
}
