"""
Django settings for OPL project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import json
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv()

#Load configuration 
with open(os.path.join(BASE_DIR,'OPL/config.json')) as file: 
    configuration = json.load(file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ.get('HOME_IP'), 'localhost', "127.0.0.1",
                 "admin.longevityknowledge.app", os.environ.get("HOST_HEADER")]  # Server IP - set to env variable
# BIND = ['0.0.0.0']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "open_problems",
    "posts_comments",
    "annotations",
    "corsheaders",
    "mptt"

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", f'http://{os.environ.get("HOME_IP")}', 'http://127.0.0.1:8000',
                        'https://www.longevityknowledge.app', 'https://admin.longevityknowledge.app',"http://79.99.42.79"]  # Home address
CSRF_TRUSTED_ORIGINS = ["https://admin.longevityknowledge.app", "http://79.99.42.79"]
REST_FRAMEWORK = {"DEFAULT_PERMISSION_CLASSES": [
    "rest_framework.permissions.AllowAny"]}

ROOT_URLCONF = "OPL.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates"), BASE_DIR/"questions"/"templates"],
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

WSGI_APPLICATION = "OPL.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('POSTGRES_USER'),
        "PASSWORD": os.environ.get('POSTGRES_PASSWORD'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": "5432"
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Set 'SECURE_PROXY_SSL_HEADER' to tell Django that the connection is HTTPS even if it's forwarded by a proxy.
http_protocol = configuration['settings']['httpProtocol']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', http_protocol)

# Set 'SESSION_COOKIE_SECURE' and 'CSRF_COOKIE_SECURE' to True to ensure cookies are only sent over HTTPS.
session_cookie_secure = eval(configuration['settings']['session_cookie_secure'])
csrf_cookie_secure = eval(configuration['settings']['csrf_cookie_secure'])
SESSION_COOKIE_SECURE = session_cookie_secure
CSRF_COOKIE_SECURE = csrf_cookie_secure

session_cookie_domain = configuration['settings']['session_cookie_domain']
SESSION_COOKIE_DOMAIN = session_cookie_domain

CSRF_TRUSTED_ORIGINS=['https://admin.longevityknowledge.app', f"http://{os.environ.get('HOME_IP')}", 'http://localhost', "http://127.0.0.1"]