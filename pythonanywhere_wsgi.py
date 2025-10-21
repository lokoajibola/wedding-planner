import os
import sys

# Add your project directory to the sys.path
path = '/home/lokoaji/wedding_planner'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'wedding_planner.settings'

# Import Django and set up
import django
django.setup()

# Import your WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()