import pytest
from django.contrib.auth.models import User, Permission, ContentType
from django.test import Client

from Bookies.models import Book, Category, Author


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    models = ContentType.objects.filter(app_label='accounts')
    bv = Permission.objects.filter(content_type__in=models)
    user = User.objects.create(username='user1')
    user.set_password('tymczasowe')
    user.user_permissions.set(bv)
    user.save()
    return user


@pytest.fixture
def categories():
    eq_list = []
    for category in range(1, 5):
        n = Category.objects.create(name=f'categories{category}')
        eq_list.append(n)
    return eq_list


@pytest.fixture
def authors():
    eq_list = []
    for author in range(1, 5):
        n = Author.objects.create(name=f'{author}')
        eq_list.append(n)
    return eq_list


@pytest.fixture
def books():
    author = Author.objects.create(name='author')
    eq_list = []
    for book in range(1, 5):
        n = Book.objects.create(title=f'books{book}', description="some",
                                author=author,
                                price='2',
                                available='True')
        eq_list.append(n)
    return eq_list
