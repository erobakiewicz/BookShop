web: gunicorn BookShop.wsgi --timeout 15 --keep-alive 5
worker: celery -A Bookshop worker --beat
release: python manage.py migrate