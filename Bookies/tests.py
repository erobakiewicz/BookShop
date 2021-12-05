from django.test import TestCase

from Bookies.factories import AuthorFactory, CategoryFactory, BookFactory


class BookiesTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author1 = AuthorFactory()
        cls.category1 = CategoryFactory()
        cls.book1 = BookFactory()

    def test_book_list_view(self):
        response = self.client.get('/bookies/all/')
        self.assertEqual(response.status_code, 200)

    def test_categories_list_view(self):
        response = self.client.get('/bookies/categories/')
        self.assertEqual(response.status_code, 200)

    def test_author_list_view(self):
        response = self.client.get('/bookies/authors/')
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view(self):
        response = self.client.get('/bookies/all/{}/'.format(self.book1.slug))
        self.assertEqual(response.status_code, 200)
