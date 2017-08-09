import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '90n+nz(*_#k*k$wcn7fdjuvtf!)c5#)yv!8zlx48shjntn%0m+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'USER': '',
           'NAME': 'Univentures',
       }
   }


INSTALLED_APPS += (
    'autofixture',
)

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, os.pardir, 'frontend', 'build'),
)
