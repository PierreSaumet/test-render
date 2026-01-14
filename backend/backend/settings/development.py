from backend.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-#ql2s$^5o(obp8!$rccmwkj&=*-k2%htndq7w=i7w0_q2y6&8x'

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# CORS_ORIGIN_ALLOW_ALL = True
# qui peut faire des requetes depuis l'exterieur
CORS_ALLOWED_ORIGINS = ['http://localhost:5173', 'http://127.0.0.1:5173']
