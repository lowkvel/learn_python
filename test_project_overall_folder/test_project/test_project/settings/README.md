# settings refactoration

1. create folder named 'settings'
2. move settings.py into the settings folder and rename it into base.py
3. create new files called dev.py, prod.py, jenkins.py, stage.py
4. type in 'from .base import *' into the files created above
5. modify manage.py, asgi.py, wsgi.py as following:
   profile = os.environ.get('TEST_PROJECT_PROFILE', 'dev')
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings.%s' %profile)
