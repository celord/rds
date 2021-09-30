from routeds.models import Eventum, NumLine, Client, Tec, RouteDistinguiser
import random
import django
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'routeds.settings')

# Import settings
django.setup()

