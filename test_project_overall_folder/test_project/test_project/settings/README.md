# settings.py refactoration

1. create folder named 'settings'
2. copy settings.py into the settings folder and rename it into base.py, then rename settings.py into old.settings.py
3. create new empty file called __init__.py inside of settings folder
4. create new files called dev.py, prod.py, jenkins.py, stage.py inside of settings folder
5. type in 'from .base import *' into the 4 files created in step 3
6. add another '.parent' to BASE_DIR in base.py
7. use 'python manage.py runserver --settings=mnyf.settings.dev' to run the project

# INSTALLED_APPS refactoration
1. split INSTALLED_APPS into APPS_PREREQUISITES and APPS_PROJECT
2. then INSTALLED_APPS = APPS_PREREQUISITES + APPS_PROJECT


