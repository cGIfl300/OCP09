"""
WSGI config for OCP09 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from OCP09.settings import MEDIA_ROOT, STATIC_ROOT, BASE_DIR

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OCP09.settings")

application = WhiteNoise(get_wsgi_application(), root=STATIC_ROOT)
application.add_files(MEDIA_ROOT, prefix='media/')
application.add_files(BASE_DIR / "static", prefix='static/')
