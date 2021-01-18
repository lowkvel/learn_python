from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

"""
# mysql configuration
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
"""

REDIS_URL = 'redis://127.0.0.1:6379'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': 'redis2333',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}

THEME = 'bootstrap'

