import os
from pathlib import Path

from dotenv import dotenv_values

config = dotenv_values(".env")

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-o#zup200eb=2f@80#j$+6wu!2x9ts-6xczkgcd%aerj2*8kh!="

DEBUG = True

# ALLOWED_HOSTS = [
#     "65.20.73.247",
#     "localhost",
# # SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    "65.20.73.247",
    "localhost",
    '127.0.0.1'
]


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
PASSWORD_RESET_TIMEOUT = 900


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.oecindia@gmail.com"
EMAIL_HOST_PASSWORD = "ktbiipsiktogqhwo"
EMAIL_USE_TLS = True

# gmail password: oecindia@123


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

# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True

# CSRF_TRUSETED_ORIGINS = ALLOWED_HOSTS
# CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
# CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_SAMESITE = None
CORS_ALLOW_ALL_ORIGINS = True


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
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
