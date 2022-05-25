import sys
import os

from django.core.wsgi import get_wsgi_application

path = "/var/www/alkisguiden"
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alcoprice.settings")

application = get_wsgi_application()
