import pytest
from django.urls import reverse

# simple http response 200 tests
from Bookies.models import Category, Book, Author


@pytest.mark.django_db
def test_views_allbooks(client):
    response = client.get(reverse("allbooks"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_views_authors(client):
    response = client.get(reverse("authors"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_views_about(client):
    response = client.get(reverse("about"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_views_contact(client):
    response = client.get(reverse("contact"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_views_categories(client):
    response = client.get(reverse("categories"))
    assert response.status_code == 200


# login user view tests
@pytest.mark.django_db
def test_cart_view(client, user):
    client.login(username='user1', password='tymczasowe')
    response = client.get(reverse('cart_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_checkout_view(client, user):
    client.login(username='user1', password='tymczasowe')
    response = client.get(reverse('registration'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_checkout_view(client, user):
    client.login(username='user1', password='tymczasowe')
    response = client.get(reverse('changepassword'))
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_views_editauthor(client):
#     response = client.get(reverse("editauthor", args=(1,)))
#     assert response.status_code == 200
#     # dla każdego testu stworzyć fixturę obiektów z PK


# # tests for instances
@pytest.mark.django_db
def test_createbook_view(client, books):
    author = Author.objects.create(name='author')
    response = client.post(reverse('createbook'), {'title': 'book_test',
                                                   'description': "some",
                                                   "author": author,
                                                   'price': '2',
                                                   'available': 'True',
                                                   'img': '',
                                                   'category': 'none',
                                                   'order': 'none'
                                                   })
    # Book.objects.get(title='book_test')
    assert response.status_code == 302


@pytest.mark.django_db
def test_createcategory_view(client, categories):
    response = client.post(reverse('createcategory'), {'name': 'category_test'})
    Category.objects.get(name='category_test')
    assert response.status_code == 302


@pytest.mark.django_db
def test_createauthor_view(client, authors):
    response = client.post(reverse('createauthor'), {'name': 'author_test', 'description': "some", 'img': ""})
    Author.objects.get(name='author_test')
    assert response.status_code == 302
