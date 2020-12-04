web: gunicorn BookShop.wsgi
worker: celery -A BookShop worker -B --loglevel=info
release: python manage.py migrate