import pytest

from Bookies.models import Book


@pytest.fixture
def test_book():
    test_book1 = Book.objects.create(title="Test_book1")
    return test_book1
