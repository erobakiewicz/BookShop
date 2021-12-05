from django.contrib import admin

from .models import Book, Author, Order, Category, OrderItem, Review


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'available']
    search_fields = ['title', 'author', 'category']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['order_item', 'rating']
    prepopulated_fields = {'slug': ('order_item',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']
    search_fields = ['user']
