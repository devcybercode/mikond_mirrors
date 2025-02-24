from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-f$g05fz^h%+x%t0**6iq1@p1spnjgd$_9!f@puv%h_qa#$cj_g'

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'fontawesomefree',

    "web.apps.WebConfig",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

SESSION_COOKIE_AGE = 8 * 24 * 60 * 60

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "web/templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mirrors',
        'USER': 'root',
        'PASSWORD': 'dimatop12',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'EN-RU'

# gettext = lambda s: s

# LANGUAGES = [
#     ('en', gettext('English')),
#     ('ru', gettext('Russian')),
# ]

# LOCALE_PATHS = [
#     BASE_DIR / "web" / "locale"
# ]

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'


TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = BASE_DIR / 'assets',

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#         'height': 600,
#         'width': '100%'
#     },
# }

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'web.UserModel'

DATA_UPLOAD_MAX_MEMORY_SIZE = 20 * 1024 * 1024

MIKOND_TELEGRAM_BOT_TOKEN="7681718288:AAGmEHn7rRXJDkuPn4FULmPb1cM4dZ-nDQY" 
MIKOND_TELEGRAM_CHAT_ID="2005608695"
# LOGIN_URL = 'main:login'