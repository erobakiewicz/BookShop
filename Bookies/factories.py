import factory
from factory import fuzzy

from Bookies.models import Book, Category, Author


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category


class BookFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(AuthorFactory)
    price = fuzzy.FuzzyDecimal(10.0,100.0, 2)
    available = True
    title = fuzzy.FuzzyText("book", 10)

    class Meta:
        model = Book

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)


