from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'root2333',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        #'CONN_MAX_AGE': 5*60,
        #'OPTIONS': {'charset': 'utf8mb4'}
    }
}


