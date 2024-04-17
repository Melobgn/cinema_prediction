"""
WSGI config for cinapps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / '.env'

dotenv.read_dotenv(ENV_FILE_PATH, override=True)
DEBUG = os.environ.get('DEBUG') == '1'

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinapps.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinapps.settings.prod")
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinapps.settings.settings')

application = get_wsgi_application()