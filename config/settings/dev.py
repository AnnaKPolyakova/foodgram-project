from .base import *

DEBUG = True

INSTALLED_APPS += [
]

#  подключаем движок filebased.EmailBackend
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# указываем директорию, в которую будут складываться файлы писем
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]