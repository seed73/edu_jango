"""
Django settings for jango_edu project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nwo18nk)pa=fku@b7$z-q6zw_j9fhjkd#9jx2lssuzs&kijj2z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'mozilla_django_oidc',
    'keycloak_auth',
    'drf_yasg',
    'auth_app',
    'student',
    'student_manage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh',
]

ROOT_URLCONF = 'jango_edu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'jango_edu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

db_name = config('DB_NAME')
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_host = config('DB_HOST')
db_port = config('DB_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
        'OPTIONS': {
            'options': '-c search_path=edu'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'auth_app.keycloak_backend.KeycloakBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'auth_app.keycloak_backend.KeycloakBackend',
    ]
}

OIDC_RP_CLIENT_ID = 'eduplex_account'
OIDC_RP_CLIENT_SECRET = 'MIICrTCCAZUCBgGKQBO1ezANBgkqhkiG9w0BAQsFADAaMRgwFgYDVQQDDA9lZHVwbGV4X2FjY291bnQwHhcNMjMwODI5MDY1NDA4WhcNMzMwODI5MDY1NTQ4WjAaMRgwFgYDVQQDDA9lZHVwbGV4X2FjY291bnQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCGhVe7Gs6AMpcGVH4bmhGEwxC1J2aWt9/NUVGg9hUmKGNYtNhcY0ozYzA5zwJv6ZNHDUvwPENCpRKTdXRsN7pkF86FwenhkorKpa+x5ZdESMAbEgEH73eUZFgFj6NGyDjb+4g8VOpGDniR1DXcN5rcYNC97tAh7Iq5W5a6NRuoN7+KHejg96RdNIIa0Wx56kPCCrWQ0AQCyxLG+OtN+ptO+7e5lGdGd1Ow5MRqrrLLEWxaWZUeV6Y34foc9F9tnZ/PLtGmUJffUnB7c07zTuaEJ6Xd6ruqYx/EgPScZEs8yTWJhUbSXs0PHsJoQm0IZ8nOB/vR3kF9ev6pI9jLBpbpAgMBAAEwDQYJKoZIhvcNAQELBQADggEBACIhD3jRD68TNqXLE6N1VIwyuBxY3IyXY6t1ulq7gVWWsYEhtLnX1Ak1VbaZml9AmIVzW2eVYBHTOHV2OjusD8WQB2oUNZm97H1XzQO0BEr1sD1dMNi7LpgJUIV8M7b6k+Acfro+3zA0dKm/CL3j+/BTQ7NOCvDpzlDCbC4zg366WWRqbyBWWpHJi2c21JQHMbu6n7kwwIXIkaN+NB2g+QXUVySq4HDkbK+/A1wfsaohYxs25Se+rcdrRjqSVftH9aIECf9B1djS/G+qKmwm5lUVsYDoPEVmosFNKRIzK+aHrZZtOc5A7M51nV5UJT8AQkaBI9zk+5ZJyAF5Q71c2h0='

OIDC_OP_AUTHORIZATION_ENDPOINT = 'http://seed32.synology.me:31479/auth/realms/edu/protocol/openid-connect/auth'
OIDC_OP_TOKEN_ENDPOINT = 'http://seed32.synology.me:31479/auth/realms/edu/protocol/openid-connect/token'
OIDC_OP_USER_ENDPOINT = 'https//http://seed32.synology.me:31479/auth/realms/edu/protocol/openid-connect/userinfo'
OIDC_OP_JWKS_ENDPOINT = 'https//http://seed32.synology.me:31479/auth/realms/edu/protocol/openid-connect/certs'
OIDC_OP_LOGOUT_ENDPOINT = 'http://seed32.synology.me:31479/auth/realms/edu/protocol/openid-connect/logout'

OIDC_RP_SIGN_ALGO = 'RS256'

SWAGGER_SETTINGS = {
      'SECURITY_DEFINITIONS': {
         'DRF Token': {
               'type': 'apiKey',
               'name': 'Authorization',
               'in': 'header'
         }
      }
   }