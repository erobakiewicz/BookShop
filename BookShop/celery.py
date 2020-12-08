import os
from celery import Celery

from BookShop import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookShop.settings')

app = Celery('BookShop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


broker_url = os.environ.get('CLOUDAMQP_URL')
broker_pool_limit = 1 # Will decrease connection usage
broker_heartbeat = None # We're using TCP keep-alive instead
broker_connection_timeout = 30 # May require a long timeout due to Linux DNS timeouts etc
result_backend = None # AMQP is not recommended as result backend as it creates thousands of queues
event_queue_expires = 60 # Will delete all celeryev. queues without consumers after 1 minute.
worker_prefetch_multiplier = 1 # Disable prefetching, it's causes problems and doesn't help performance
worker_concurrency = 50 # If you tasks are CPU bound, then limit to the number of cores, otherwise increase substainally