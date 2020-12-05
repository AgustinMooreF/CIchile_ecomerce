from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'grupo12',
        'USER' : 'grupo12',
        'PASSWORD' : '18635317K',
        'DEFAULT-CHARACTER-SET' : 'utf8',
        'HOST' : 'grupo12.c5d4mi2dthpc.us-east-1.rds.amazonaws.com',
        'PORT' : '3306',
        'TEST': {
            'NAME': 'planificacion_test',
        }
    },
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
STATIC_ROOT="/store/static"
#ADMIN_ENABLED=False
DEBUG=False
SECRET_KEY=os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']
USE_X_FORWARDED_HOST=True
USE_X_FORWARDED_PORT=True

INSTALLED_APPS += ('corsheaders',)
MIDDLEWARE += ('corsheaders.middleware.CorsMiddleware',)
CORS_ORIGIN_ALLOW_ALL = True
