# -*- coding: utf-8 -*-
import socket
import os

from django.core.urlresolvers import reverse_lazy

gettext = lambda s: s

DEBUG = True


# PATHS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = BASE_DIR
PROJECT_PATH = ROOT_PATH
PROJECT_NAME = os.path.basename(ROOT_PATH)
PROJECT_DATA_DIR = os.path.join(BASE_DIR, PROJECT_NAME, 'data')
__TEMPLATE_DIR = os.path.join(BASE_DIR, PROJECT_NAME, 'templates')

VIRTUAL_ENV_DIR = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))
LOGGING_DIR = os.path.join(VIRTUAL_ENV_DIR, 'log')

STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_URL = '/media/'

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'frontend/static/frontend')

LOCAL_SETTINGS_FILE = os.path.join(BASE_DIR, PROJECT_NAME, 'local_settings.py')
SECRET_SETTINGS_FILE = os.path.join(BASE_DIR, PROJECT_NAME, 'secret_settings.py')


# ------
for path in [LOGGING_DIR, STATIC_ROOT, MEDIA_ROOT, BOWER_COMPONENTS_ROOT, PROJECT_DATA_DIR, __TEMPLATE_DIR]:
    if not os.path.exists(path):
        os.makedirs(path, mode=0o755, exist_ok=True)

if not os.path.exists(SECRET_SETTINGS_FILE):
    with open(SECRET_SETTINGS_FILE, 'w') as f:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        f.write('# -*- coding: utf-8 -*-\n')
        f.write("SECRET_KEY = '%s'\n" % get_random_string(50, chars))
        f.write("DB_PASSWORD = '%s'\n" % get_random_string(50))
        f.write("EMAIL_HOST_PASSWORD = '%s'\n" % get_random_string(50))
        f.close()

if not os.path.exists(LOCAL_SETTINGS_FILE):
    with open(LOCAL_SETTINGS_FILE, 'w') as f:
        f.write('# -*- coding: utf-8 -*-\n')
        f.close()

from .secret_settings import *

# HOSTS
HOSTNAME = socket.gethostname()
RELEASE_HOSTS = [
    'hatebase',
    # 'haterelay',
]

ALLOWED_HOSTS = [
    HOSTNAME,
    '127.0.0.1',
]

if HOSTNAME in RELEASE_HOSTS:
    DEBUG = False


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'django.contrib.sites',

    'djangobower',
    'frontend',
    'django_dbdump',
    'django_congen',
]


BOWER_INSTALLED_APPS = (
    'jquery',
    'materialize',
    'select2',
    'js-cookie',
)


JQUERY_URL = '/static/frontend/bower_components/jquery/dist/jquery.min.js'


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',

    # 'htmlmin.middleware.HtmlMinifyMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'csp.middleware.CSPMiddleware',
    # 'htmlmin.middleware.MarkRequestMiddleware',
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [__TEMPLATE_DIR],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                # 'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': ''
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': '{{ project_name }}',
    },

    'persistent': {
        'KEY_PREFIX': '{{ project_name }}',
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            'localhost:6379',
        ],
        'OPTIONS': {
            'DB': 8,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'PICKLE_VERSION': 2,
        },
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_SAVE_EVERY_REQUEST

# if HOSTNAME in RELEASE_HOSTS:
#     CACHES['persistent']['OPTIONS']['PASSWORD'] = '111'


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


LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('en', gettext('en')),
    ('ru', gettext('ru')),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# BATTERIES
# =========

# django cspreports
CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com', "'unsafe-inline'")
CSP_SCRIPT_SRC = ("'self'", '*.yandex.ru', '*.google.com', "'unsafe-inline'", "'unsafe-eval'")
CSP_FONT_SRC = ("'self'", '*.gstatic.com')
CSP_IMG_SRC = ("'self'", '*.yandex.ru', '*.paypal.com', '*.gstatic.com')
CSP_FRAME_SRC = ("*.youtube.com", "*.google.com")
CSP_CONNECT_SRC = ('*.yandex.ru', "'self'")
CSP_REPORT_URI = reverse_lazy('report_csp')
CSP_REPORTS_LOGGER_NAME = 'raven'
CSP_REPORTS_EMAIL_ADMINS = True


# REDEFINE
from .local_settings import *
