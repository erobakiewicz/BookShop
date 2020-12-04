web: gunicorn BookShop.wsgi --timeout 15 --keep-alive 5
worker: celery -A BookShop worker -B --loglevel=info
release: python manage.py migrate