import os, sys
sys.path.insert(0, '/var/www/u1359685/data/www/torpeda.xyz/dartblog')
sys.path.insert(1, '/var/www/u1359685/data/djangoenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dartblog.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()