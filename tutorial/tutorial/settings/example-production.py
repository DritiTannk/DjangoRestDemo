from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7ph))na+2i1sr8)^p=ozr9f_-7yzbz+go*r&llywa&0x90(r!q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

