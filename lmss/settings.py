from pathlib import Path

from dotenv import dotenv_values

config = dotenv_values(".env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-o#zup200eb=2f@80#j$+6wu!2x9ts-6xczkgcd%aerj2*8kh!="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["65.20.73.247", "localhost"]


# Application definition

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
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
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
        "DIRS": [],
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


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "staticfiles/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_ROOT = "/var/www/static/"
MEDIA_ROOT = "/var/www/media/"

PASSWORD_RESET_TIMEOUT = 900


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "mehulmac777@gmail.com"
EMAIL_HOST_PASSWORD = "096380309561"
EMAIL_USE_TLS = True

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

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    "APPEND_SLASH": True,
}

APPEND_SLASH = True
