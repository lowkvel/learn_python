"""
ASGI config for test_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

profile = os.environ.get('TEST_PROJECT_PROFILE', 'dev')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings.%s' %profile)

application = get_asgi_application()
