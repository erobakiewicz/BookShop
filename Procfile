web: gunicorn BookShop.wsgi --timeout 150 --keep-alive 50
worker: python manage.py celery worker -B -l info
release: python manage.py migrate
