import os, sys

sys.path.append('/var/www')
sys.path.append('/var/www/instashop')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instashop.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()