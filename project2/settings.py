import os   # Import dj-database-url at the beginning of the file.
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'django-insecure-lwd7pzt&(6*6^l8lmwoz6fdcrznsf959hzo%6*-4wuxltu4(0^'

# SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = 'True'

#os.environ.get("DEBUG", "False").lower() == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(" ")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api.apps.ApiConfig',
    
    'rest_framework',
    'rest_framework.authtoken',


    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # add this line to enable CORS headers
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
    

]


CORS_ORIGIN_ALLOW_ALL = True  # If you want to allow all origins
# OR
CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',  # Replace with the actual origin of your React app
]

ROOT_URLCONF = 'project2.urls'

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

WSGI_APPLICATION = 'project2.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':'db.sqlite3',
    }
}

#DATABASES = {
#   'default': {

      #  'ENGINE': 'mysql.connector.django',

      #  'NAME': 'AmiraDB',
      #  'USER': 'testuser',
      #  'PASSWORD': '302569',
      #  'HOST': '127.0.0.1',
      #  'PORT': '3307',
#    }
#
#}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True #

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = "/media/"

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#SMTP Conf: (YOU ORG REAL EMAIL TO BE USED HERE AUTO)

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT ='587'                                     #for TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER ='ahmedeid2504@gmail.com'             #ur email
EMAIL_HOST_PASSWORD ='rpsz xokc pfsk aghw'         #ur password

