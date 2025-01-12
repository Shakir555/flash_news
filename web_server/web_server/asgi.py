# Libraries
import os
from django.core.asgi import get_asgi_application

# ASGI Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_server.settings')
application = get_asgi_application()
