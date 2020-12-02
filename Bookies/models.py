from django.contrib.auth.models import User, Permission
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg, Sum
from django.urls import reverse
from django.utils.text import slugify

from Bookies.constants import OrderStatuses


# book model

class Book(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    available = models.BooleanField()
    img = models.ImageField(blank=True, null=True, upload_to='img', default='book_default.jpg')
    category = models.ManyToManyField("Category")
    order = models.ManyToManyField("Order", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'id'

    @property
    def rating(self):
        return Review.objects.filter(order_item__book_id=self, order_item__order__status=30).aggregate(
            Avg('rating')).get('rating__avg')



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

# Author model
class Author(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    description = models.TextField()
    img = models.ImageField(blank=True, null=True, upload_to='img', default='writer_default.jpg')

    def __str__(self):
        return self.name


# Category model
class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=255, null=True, unique=True)


    def __str__(self):
        return self.name


# Review model
class Review(models.Model):
    order_item = models.OneToOneField("OrderItem", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    comment = models.TextField()

    def __str__(self):
        return str(self.order_item)


# Order / OrderItem models
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.PositiveSmallIntegerField(choices=OrderStatuses.Choices)
    price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0.01)])

    def __str__(self):
        return self.user.username

    @classmethod
    def get_editable_order(cls, user):
        order = cls.objects.filter(user=user, status=OrderStatuses.EDITABLE)
        if order.count() == 0:
            order = cls.objects.create(user=user, status=OrderStatuses.EDITABLE)
        elif order.count() > 1:
            raise Exception(f'This user has more than one editable order. \
                User {user.id}, Order ids {", ".join(str(id) for id in order.values_list("id", flat=True))}')
        else:
            order = order.last()
        return order

    @property
    def get_total_price(self):
        return self.ordered_items.aggregate(total_price=Sum('book__price')).get('total_price', 0)

    def close_order(self):
        self.status = OrderStatuses.COMLETED
        self.total_price = self.get_total_price
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey("Order", related_name='ordered_items', on_delete=models.CASCADE)
    book = models.ForeignKey("Book", related_name='ordered_items', on_delete=models.PROTECT)

    def __str__(self):
        return self.book.title

    class Meta:
        get_latest_by = 'id'
