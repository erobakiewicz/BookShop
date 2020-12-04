web: gunicorn BookShop.wsgi --timeout 15 --keep-alive 5
worker: celery worker --app=tasks.app--loglevel=info
release: python manage.py migrate