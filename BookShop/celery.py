import os
from celery import Celery

from BookShop import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookShop.settings')

app = Celery('BookShop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

broker_url = os.environ.get('CLOUDAMQP_URL')
# Will decrease connection usage
broker_pool_limit = 1
# We're using TCP keep-alive instead
broker_heartbeat = None
# May require a long timeout due to Linux DNS timeouts etc
broker_connection_timeout = 30
# AMQP is not recommended as result backend as it creates thousands of queues
result_backend = None
# Will delete all celeryev. queues without consumers after 1 minute.
event_queue_expires = 60
# Disable prefetching, it's causes problems and doesn't help performance
worker_prefetch_multiplier = 1
# If you tasks are CPU bound, then limit to the number of cores,
# otherwise increase substantially
worker_concurrency = 50
