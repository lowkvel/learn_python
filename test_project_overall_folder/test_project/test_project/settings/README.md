# settings.py refactoration

1. create folder named 'settings'
2. move settings.py into the settings folder and rename it into base.py
3. create new empty file called __init__.py inside of settings folder
4. create new files called dev.py, prod.py, jenkins.py, stage.py inside of settings folder
5. type in 'from .base import *' into the 4 files created in step 3
6. modify manage.py, asgi.py, wsgi.py as following to use dev environment:
   profile = os.environ.get('TEST_PROJECT_PROFILE', 'dev')
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings.%s' %profile)

# INSTALLED_APPS refactoration
1. split INSTALLED_APPS into APPS_PREREQUISITES and APPS_PROJECT
2. then INSTALLED_APPS = APPS_PREREQUISITES + APPS_PROJECT


