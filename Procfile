web: gunicorn BookShop.wsgi --timeout 15 --keep-alive 5
worker: python manage.py celery worker -B -l info
release: python manage.py migrate