import os
from celery import Celery

from BookShop import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookShop.settings')

app = Celery('BookShop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)