import os
from pathlib import Path
from dotenv import load_dotenv
import django
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str
from django.utils.translation import gettext
django.utils.translation.ugettext = gettext

# Carregar as variáveis de ambiente do arquivo .env
BASE_DIR = Path(__file__).resolve().parent.parent

# Carregar o arquivo .env
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.parent / 'data' / 'web'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "web",
    "54.232.202.170",
    "sistemaunasus.ufam.edu.br",
]

# Configuração CORS para aceitar todas as origens
CORS_ALLOW_ALL_ORIGINS = True

"""
Configurações de HTTPS e Segurança (Desabilitado para Desenvolvimento)

SECURE_SSL_REDIRECT = True  # Redireciona automaticamente HTTP para HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Suporte para HTTPS atrás de um proxy
SECURE_HSTS_SECONDS = 31536000  # Habilita HTTP Strict Transport Security (1 ano)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Inclui subdomínios no HSTS
SECURE_HSTS_PRELOAD = True  # Prepara o site para a lista HSTS Preload
SECURE_BROWSER_XSS_FILTER = True  # Proteção contra XSS no navegador
SECURE_CONTENT_TYPE_NOSNIFF = True  # Bloqueia tipos de conteúdo inseguros
CSRF_COOKIE_SECURE = True  # Torna o cookie de CSRF acessível apenas via HTTPS
SESSION_COOKIE_SECURE = True  # Torna o cookie de sessão acessível apenas via HTTPS
X_FRAME_OPTIONS = 'DENY'  # Evita que o site seja carregado em um iframe (cliquejacking)
CSRF_TRUSTED_ORIGINS = ['https://sistemaunasus.ufam.edu.br']  # Apenas se necessário para produção

"""


SIMPLE_JWT = {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
}

INSTALLED_APPS = [
    'unasus_registros',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Adicione o middleware do corsheaders aqui
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_ALLOW_REFRESH': True,
}

WSGI_APPLICATION = 'project.wsgi.application'

# Database
if os.getenv('ENVIRONMENT', 'development') == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB_LOCAL'),
            'USER': os.getenv('POSTGRES_USER_LOCAL'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD_LOCAL'),
            'HOST': os.getenv('POSTGRES_HOST_LOCAL'),
            'PORT': os.getenv('POSTGRES_PORT_LOCAL'),
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB_PROD'),
            'USER': os.getenv('POSTGRES_USER_PROD'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD_PROD'),
            'HOST': os.getenv('POSTGRES_HOST_PROD'),
            'PORT': os.getenv('POSTGRES_PORT_PROD'),
        },
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
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
AUTH_USER_MODEL = 'unasus_registros.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
