"""
WSGI config for test_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior
# test_project directory.
app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
sys.path.append(os.path.join(app_path, 'test_project'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

application = get_wsgi_application()
