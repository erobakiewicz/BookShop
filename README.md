# Bookers - online ebook store
Bookers web app of online ebook store. Registered users can purchase books and write reviews.

# See the app on Heroku
<a href="https://ebookstorebookers.herokuapp.com">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

# Functionalities
The app is written in python using the Django framework and Bootstrap and AWS S3 (serving static files)     .

# User management:
- guest view, log-in, and log-out
- registration
- user profile update and delete
- user profile lists purchased books
- password change

# General functionalities:
- CRUD for all the books, categories and authors
- users can write reviews of purchased books
- average rating for books
- search engine for books
- pagination for books and authors
- landing page includes 5 newest books and 4 newest reviews

# requirements.txt
```sh
amqp==2.6.1
appdirs==1.4.3
asgiref==3.2.10
attrs==20.2.0
Babel==2.9.0
billiard==3.6.3.0
boto==2.49.0
boto3==1.15.16
botocore==1.18.16
CacheControl==0.12.6
celery==4.4.2
certifi==2019.11.28
cffi==1.14.4
chardet==3.0.4
colorama==0.4.3
contextlib2==0.6.0
distlib==0.3.0
distro==1.4.0
dj-config-url==0.1.1
dj-database-url==0.5.0
Django==3.1.2
django-environ==0.4.5
django-storages==1.10.1
factory-boy==3.2.1
Faker==9.9.0
flake8==4.0.1
flower==0.9.3
gunicorn==20.0.4
html5lib==1.0.1
idna==2.8
iniconfig==1.0.1
ipaddr==2.2.0
jmespath==0.10.0
kombu==4.6.11
lockfile==0.12.2
mccabe==0.6.1
msgpack==0.6.2
packaging==21.3
pep517==0.8.2
pika==1.1.0
Pillow==7.2.0
pluggy==0.13.1
progress==1.5
psycopg2-binary==2.8.6
py==1.9.0
pycodestyle==2.8.0
pycparser==2.20
pyflakes==2.4.0
pyparsing==2.4.7
pytest==6.1.0
python-dateutil==2.8.1
pytoml==0.1.21
pytz==2020.1
rabbitmq==0.2.0
requests==2.22.0
retrying==1.3.3
s3transfer==0.3.3
six==1.15.0
sqlparse==0.3.1
text-unidecode==1.3
toml==0.10.1
tornado==5.1.1
urllib3==1.25.10
vine==1.3.0
webencodings==0.5.1
whitenoise==5.2.0
```
