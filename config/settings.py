from pathlib import Path
import dotenv
import os

from django.contrib import admin
from datetime import timedelta

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG_STATE') == 'True'

ALLOWED_HOSTS = [
    '*',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'djoser',
    'django_filters',
    'djrichtextfield',
    'django_user_agents',
    'nested_inline',

    'users.apps.UsersConfig',

    'product',
    'order',
    'cart'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

DEPLOY_STATE = os.environ.get('DEPLOY_STATE') == 'True'

if DEPLOY_STATE:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DATABASES_ENGINE'),
            'NAME': os.environ.get('DATABASES_NAME'),
            'USER': os.environ.get('DATABASES_USER'),
            'PASSWORD': os.environ.get('DATABASES_PASSWORD'),
            'HOST': os.environ.get('DATABASES_HOST'),
            'PORT': os.environ.get('DATABASES_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ADMIN_URL = os.environ.get('ADMIN_URL')
PROJECT_NAME_URL_PARAM = os.environ.get('PROJECT_NAME_URL_PARAM')
ADMIN_SITE_HEADER = os.environ.get('ADMIN_SITE_HEADER')
ADMIN_SITE_TITLE = os.environ.get('ADMIN_SITE_TITLE')
ADMIN_INDEX_TITLE = os.environ.get('ADMIN_INDEX_TITLE')

STATIC_URL = os.environ.get('STATIC_URL')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_dir'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = os.environ.get('MEDIA_URL')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]
# from rest_framework.renderers
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/min',
        'user': '1000/min',
    },
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': '/' + ADMIN_URL,
    'LOGOUT_URL': '/' + ADMIN_URL + 'logout/',
    'USE_SESSION_AUTH': True,
}
REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
    'HIDE_HOSTNAME': True,
    'REQUIRED_PROPS_FIRST': True,
}

SIMPLE_HISTORY_REVERT_DISABLED = True

APPEND_SLASH = True

EXTERNAL_REQUESTS_TIMEOUT = int(os.environ.get('EXTERNAL_REQUESTS_TIMEOUT', '10'))

# User Model Config
AUTH_USER_MODEL = 'users.User'

# Gando Config
GANDO = {
    'MONITOR_KEYS': [
        'logged_in',
    ],
    'CACHING': False,
}

# SimpleJWT Config
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_ACCESS_TOKEN_LIFETIME_MINUTES'))),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_REFRESH_TOKEN_LIFETIME_MINUTES'))),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': os.environ.get('SIMPLE_JWT_ALGORITHM'),
    'SIGNING_KEY': os.environ.get('SIMPLE_JWT_SIGNING_KEY'),
    'VERIFYING_KEY': '',
    'AUDIENCE': None,
    'ISSUER': None,
    'JSON_ENCODER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': (
        'Bearer',
    ),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    ),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_SLIDING_TOKEN_LIFETIME_MINUTES'))),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_SLIDING_TOKEN_REFRESH_LIFETIME_MINUTES'))),

    'TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
    'TOKEN_REFRESH_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenRefreshSerializer',
    'TOKEN_VERIFY_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenVerifySerializer',
    'TOKEN_BLACKLIST_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenBlacklistSerializer',
    'SLIDING_TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer',
    'SLIDING_TOKEN_REFRESH_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer',
}
