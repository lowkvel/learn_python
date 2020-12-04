# temp

# create and use a new venv for a new project
"""
Create a new directory for the project named new_dir, then cd into the directory new_dir created before
Run the command "python -m venv new_venv" to create a new venv
Run the command "source new_venv/bin/activate" to activate the new venv
Run the command "deactivate" to deactivate the new venv if needed
* the new venv folder "new_venv" will be located under new_dir
"""

# install Django for the new venv
"""
Run the command "pip install django" to install Django on current venv
* the Django packages will be located under new_dir/new_venv/...
"""

# create a .gitignore file for the project
"""
Create a file named .gitignore under the project folder
Put the following path and filename into the file
env_blog/               new_env path
__pycache__/            pycache path
*.sqlite3               databse name
.DS_Store               extras
"""

# create a Django project under the new venv
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

# create the database for the project
"""
Run the command "python manage.py migrate" to create the database
"""

# view the project on localhost, the development server
"""
Run the command "python manage.py runserver" to view the project
Run the command "python manage.py runserver port_id" on another port
"""

# going to production server
"""
In order to deploy Django in a production environment, 
run it as a WSGI application using a web server, such as Apache, Gunicorn, or uWSGI, 
or as an ASGI application using a server like Uvicorn or Daphne
"""

# start an application under the project
"""
Run the command "python manage.py startapp new_app" to start an app under the project
* the app folders "new_app" will be located under new_dir/new_project
The admin.py is where the register models to include
The apps.py includes the main configuration of the new_app
The models.py includes the data models of the new_app
The tests.py is where the tests located for the new_app
The views.py is where the new_app logic goes, each views receives an http request, process it, then returns a response
The migrations directory contains the database migrations of the new_app
"""

# defining/activating/migrating models
"""
define the models in models.py (app folder)
activating the models in settings.py (project folder)
Run the command "python manage.py makemigrations learning_logs" to make migrations (design the database modifications)
* Run the command "python manage.py sqlmigrate new_app 0001" to check the SQL code for the migrations
Run the command "python manage.py migrate" to migrate (apply the database modifications)
"""

# setting up admin, import/register models for administration
"""
Run the command "python manage.py createsuperuser" to create a superuser
import the models from models.py we want to register into admin.py by using "from .models import Topic"
register/manage the models from models.py through the admin site by using "admin.site.register(Topic)"
* no need for restarting the server
"""

# make pages, 1 defining URLs, 2 writing views, 3 writing templates
"""
defining URLs in urls.py from the project folder by using "path('', include('new_app.urls')),"
defining URLs in urls.py from the app folder by using "new_app=..., urlpatterns=[...]"
writing views in views.py from the app folder by using "render(request, template)"
writing templates in app_folder/templates/app_folder
"""



