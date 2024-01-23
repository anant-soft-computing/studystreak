import os
from pathlib import Path

from dotenv import dotenv_values
import os 
import datetime
from datetime import timedelta
config = dotenv_values(".env")
from django.conf import settings
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-o#zup200eb=2f@80#j$+6wu!2x9ts-6xczkgcd%aerj2*8kh!="

DEBUG = True

# ALLOWED_HOSTS = [
#     "65.20.73.247",
#     "localhost",
# # SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["65.20.73.247", "localhost", "127.0.0.1"]
# settings.py

ZOOM_API_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NDg5NTE5LCJpYXQiOjE3MDU0ODkyMTksImp0aSI6IjQ3MjY3NDE3MWViMjRkZGNiMTM2OGRjMTU5M2RhZTdkIiwidXNlcl9pZCI6Mn0.Gq4SNpGYNqI-nrU6G8iP902vX9SOnFIGjF_z66pzRe4'

JWT_AUTH = {
    # Authorization:Token xxx
    'JWT_AUTH_HEADER_PREFIX':'JWT',
}


INSTALLED_APPS = [
    "debug_toolbar",
    "jazzmin",
    "master",
    "Courses",
    "live_classes",
    "package",
    "students",
    "assessment",
    "coursedetail",
    "import_export",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    'rest_framework.authtoken',
    "ckeditor",
    "website",
    "CreateTest",
    "nested_admin",
    "QuestionBank",
    "Listening_Exam",
    "Reading_Exam",
    "Writing_Exam",
    "Speaking_Exam",
    "corsheaders",
    "exam",
    "froala_editor",
    "ckeditor_uploader",
    "drf_spectacular",
    "django_filters",
    'payment',
]
CKEDITOR_UPLOAD_PATH = "uploads/"
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lmss.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lmss.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config["DB_NAME"],  # "lmss",
        "USER": config["DB_USER"],
        "PASSWORD": config["DB_PASSWORD"],  # os.environ.get("DB_PASSWORD"),
        "HOST": config["DB_HOST"],
        "PORT": config["DB_PORT"],
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "staticfiles/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_ROOT = "/var/www/static/"
MEDIA_ROOT = "/var/www/media/"
MEDIA_URL = "media/"
PASSWORD_RESET_TIMEOUT = 3600


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.studystreak@gmail.com"
EMAIL_HOST_PASSWORD = "sypowsabvnbqjhrv"
EMAIL_USE_TLS = True
# REQUIRE_AUTHENTICATION = True

# gmail password: oecindia@123
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"]
}


JAZZMIN_SETTINGS = {
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        # {
        #     "name": "Support",
        #     "url": "https://github.com/farridav/django-jazzmin/issues",
        #     "new_window": True,
        # },
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {"model": "students.Student"},
        {"model": "Courses.Course"},
        {"model": "coursedetail.Lesson"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


REST_FRAMEWORK = {
    "APPEND_SLASH": True,
}

APPEND_SLASH = True


CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "extraPlugins": ",".join(
            [
                "devtools",
                "menubutton",
                "table",
                "tableresize",
                "tabletools",
            ]
        ),
    },
}

SESSION_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_HTTPONLY = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_SAMESITE = None
CORS_ALLOW_ALL_ORIGINS = True


REST_FRAMEWORK = {
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Study Streak API",
    # 'DESCRIPTION': 'Your project description',
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

PASSWORD_RESET_TIMEOUT = 60 * 30

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

DEFAULTS = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

KEY_ID="rzp_test_QyWQWfJeARzOZG"
KEY_SECRET="CbjpLbEoily2YroYWMuvNfxG"