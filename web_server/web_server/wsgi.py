# Libraries
import os
from django.core.wsgi import get_wsgi_application

# Web Server Gateway Interface Application Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_server.settings')
application = get_wsgi_application()
