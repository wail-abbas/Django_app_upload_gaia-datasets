from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8xu+^9nzl3lw#o26l918uw%1hk0d@43ofqy-5y3phq@+&mz^r^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testdb2',
        'USER': 'test1',
        'PASSWORD': 'test1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


CELERY_BROKER_URL = 'amqp://localhost' 
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'rpc://'