import os
import sys

path = "/var/www/cafe"
sys.path.append(path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'cafeapp.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


