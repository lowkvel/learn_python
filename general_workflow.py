# temp

# 0 create a folder for all code
"""
Create a new directory for the project named new_dir, 
then cd into the directory new_dir
this is the overall project folder, will contain many none-src files, such as venv folder, .gitignore, README.md, etc
"""

# 1 create and use a new venv for a new project
"""
Run the command "python -m venv new_venv" to create a new venv under the new_dir
Run the command "source new_venv/bin/activate" to activate the new venv
Run the command "deactivate" to deactivate the new venv if needed
* the new venv folder "new_venv" will be located under new_dir
"""

# 2 install Django for the new venv
"""
Run the command "pip install django" to install Django for current venv
* the Django packages will be located under new_dir/new_venv/...
"""

# 2.1 create a .gitignore file
"""
Create a file named .gitignore under the new_dir
Put the following path and filename into the file
new_env/                new_env path
__pycache__/            pycache path
*.sqlite3               databse name
.DS_Store               extras
"""

# 3 create a Django project under the new venv
"""
Run the command "django-admin startproject new_project ." to create a Django project
* the project folders "new_project" will be located under new_dir
The manage.py file is a command line utility used to interact with the project.
The __init.py__ file is an empty file simply tells python to treat the project directory as a python module.
The settings.py file indicates settings and configuration for the project.
The urls.py file tells Django which pages to build in response to browser requests. Each url defined here mapped to a view. 
The wsgi.py file is the configuration to run the project as WSGI, for web server gateway interface.
The asgi.py file is the configuration to run the project as ASGI, for asynchronous web servers and applications.
"""

# 3.1 create the database for the project
"""
Run the command "python manage.py migrate" to create the database
"""

# 3.2 view the project on localhost, the development server
"""
Run the command "python manage.py runserver" to view the project
Run the command "python manage.py runserver port_id" on another port
"""

# 3.x going to production server
"""
In order to deploy Django in a production environment, 
run it as a WSGI application using a web server, such as Apache, Gunicorn, or uWSGI, 
or as an ASGI application using a server like Uvicorn or Daphne
"""

# 4 start an application under the project
"""
CD into the folder new_dir/new_project
Run the command "python manage.py startapp new_app" to start an app under the project
* the app folders "new_app" will be located under new_dir/new_project
Adding the full app config of the local app to the end of the file settings.py
The admin.py is where the register models to include
The apps.py includes the main configuration of the new_app
The models.py includes the data models of the new_app
The tests.py is where the tests located for the new_app
The views.py is where the new_app logic goes, each views receives an http request, process it, then returns a response
The migrations directory contains the database migrations of the new_app
"""

# 5 defining/activating/migrating models
"""
define the models in models.py (app folder)
Run the command "python manage.py makemigrations learning_logs" to make migrations (design the database modifications)
* Run the command "python manage.py sqlmigrate new_app 0001" to check the SQL code for the migrations
Run the command "python manage.py migrate" to migrate (apply the database modifications)
"""

# 6 setting up admin, import/register models for administration
"""
Run the command "python manage.py createsuperuser" to create a superuser
import the models from models.py we want to register into admin.py by using "from .models import Model_name"
register/manage the models from models.py through the admin site by using "admin.site.register(Model_name)" or use "@admin.register()"
"""

# 7 make pages, 1 defining URLs, 2 writing views, 3 writing templates
"""
defining URLs in urls.py from the project folder by using "path('', include('new_app.urls')),"
defining URLs in urls.py from the app folder by using "new_app=..., urlpatterns=[...]"
writing views in views.py from the app folder by using "render(request, template)"
writing templates in app_folder/templates/app_folder
"""

# x ORM: object-relational mapper
"""
Post.objects.all()                                                          # default manager: objects. basic retrieve method
Post.objects.filter(publish__year=2020, author__username='admin')           # multiple fields filter, using field__attribute='target_value'
Post.objects.filter(publish__year=2020).exclude(title__startswith='Why')    # exclude specific results, similar to filter
Post.objects.order_by('-title')                                             # ordering in reverse order of title
post = Post.objects.get(id=1), then post.delete()                           # delete objects
"""

# some common methods in models
"""
fields
managers
class Meta
def __str__
def save
def get_absolute_url
"""

# general project structure
"""
project/                overall project folder, contains many none-code files and folders
    LICENCE             open source licences
    MANIFEST.in         along with setup.py
    README.md           introduction to the project
    conf/               configuration files, such as nginx, supervisor, etc
    fabfile/            for Fabric
    others/             docs, project requirements files, etc
    requirements.txt    dependency file list, pip install -r requirements.txt
    setup.py            used for packaging project
    .gitignore          pyc, logs, etc

    project_venv/       venv for project, "python -m venv new_venv", "source new_venv/bin/activate", "pip install django", etc
        ...

    project(src)/       source code for project, "django-admin startproject new_project ."
        project app/            normal version
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py

        project app/            advanced version used for splitting different environments
            settings/           refactoring settings.py, deleve settings.py, create settings folder
                __init__.py
                base.py         create base.py and move everything in previous settings.py into base.py
                develop.py      settings.py for development environment, from test_project.settings.base import *, then override specific part
                product.py      settings.py for production environment, from test_project.settings.base import *, then override specific part
            __init__.py
            asgi.py             modify this file if settings.py got refactored
            urls.py
            wsgi.py             modify this file if settings.py got refactored

        app1/
            ...

        app2/
            ...
        
        manage.py               modify this file if settings.py got refactored

        * wsgi.py, asgi.py and manage.py modification for settings.py refactoration
        * original:     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')
        * afterwards:   profile = os.environ.get('PROJECT_PROFILE', 'develop')
        *               os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings.%s' %profile)

"""