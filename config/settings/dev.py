from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': env('DB_NAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'DB': env('POSTGRES_DB'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# подключаем движок filebased.EmailBackend
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# указываем директорию, в которую будут складываться файлы писем
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
