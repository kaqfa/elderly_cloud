"""
Django settings for elderly_cloud project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib.messages import constants as message_constants
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4wl%q*7o14kvqoq6-c!&49vkqmcxokq#_*g6+-jy+%fx$r(u9+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 'wpadmin',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    # 'elder_profile',
    # 'feedback',
    'member',
    # 'notification',
    # 'contact',
    # 'partner',
    'article',
    'info',
    'tracker',
    'hospital',
    'rest_framework',
    'rest_framework.authtoken',
    # 'django_filters',
    'django_summernote',
    'location_field',
    'corsheaders',
)

GOOGLE_MAPS_V3_APIKEY = 'AIzaSyArVrzYHjRmxyYMhZti0v-tPLV6qVIpZEM'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
    )
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'elderly_cloud.urls'
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'elderly_cloud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'id'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIXTURE_DIRS = ('fixtures/',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_URL = '/'

# WPADMIN = {
#     'admin': {
#         # 'admin_site': 'elderly_cloud.admin.admin',
#         'title': 'Elderly Application',
#         'menu': {
#             'top': 'wpadmin.menu.menus.BasicTopMenu',
#             'left': 'wpadmin.menu.menus.BasicLeftMenu',
#         },
#         'dashboard': {
#             'breadcrumbs': True,
#         },
#         'custom_style': STATIC_URL + 'wpadmin/css/themes/ocean.css',
#     }
# }

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Administrasi Berbakti',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'app': 'member', 'icon':'icon-user', 
         'models': ('auth.user', 'member.member', 'member.elder', 'member.caregiver', 'auth.group')},        
        # {'label': 'Data Kondisi', 'icon':'icon-question-sign', 'url': '/admin/tracker/tracker/'},
        {'app': 'tracker', 'icon':'icon-signal', 'models': ('tracker.trackcondition', 'tracker.trackpanic')}, 
    ),

    # misc
    # 'LIST_PER_PAGE': 15
}

MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger'}
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@berbakti.id'
SERVER_EMAIL = 'admin@berbakti.id'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'admin@berbakti.id'
EMAIL_HOST_PASSWORD = 'Elderly_12'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

try:
    from local_settings import *
except ImportError:
    pass
