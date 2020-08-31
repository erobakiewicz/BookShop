from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView

from Bookies.models import Book, Author, Category, Review, Order, OrderItem


# book views
class BooksListView(ListView):
    model = Book
    template_name = 'all_books.html'


# detail view
class BookDetailView(DetailView):
    model = Book
    template_name = "book_details.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'reviews': Review.objects.filter(order_item__book_id=self.kwargs.get('pk'))},
        )
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'available', 'img', 'category']
    template_name = 'book_form.html'
    success_url = reverse_lazy('allbooks')


class BookEditView(UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'available', 'img', 'category']
    template_name = 'book_form.html'
    success_url = reverse_lazy('allbooks')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('allbooks')


# author views

class AuthorsTemplateView(ListView):
    model = Author
    template_name = 'authors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'authors': Author.objects.all()})
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_details.html"
    fields = '__all__'


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'description', 'img']
    template_name = 'author_form.html'
    success_url = reverse_lazy('authors')


class AuthorEditView(UpdateView):
    model = Author
    fields = ['name', 'description', 'img']
    template_name = 'author_form.html'
    success_url = reverse_lazy('authors')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('authors')


# category views

class CategoryTemplateView(ListView):
    model = Category
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'authors': Category.objects.all()})
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_details.html"
    fields = '__all__'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('categories')


class CategoryEditView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('categories')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('categories')


# about view

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


# contact view

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')


# Cart ORDER, ORDERITEM

class AddOrderItemView(View):
    def post(self, *args, **kwargs):
        order = Order.get_editable_order(self.request.user)
        OrderItem.objects.create(
            book_id=self.kwargs.get('book_id'),
            order=order,
        )
        return redirect('allbooks')


class DeleteOrderItemView(DeleteView):
    model = OrderItem
    template_name = 'orderitem_confirm_delete.html'
    success_url = reverse_lazy('cart_view')


class CartView(TemplateView):
    model = Order
    template_name = 'cart.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['order'] = Order.get_editable_order(self.request.user)
        return ctx


class Checkout(View):
    def post(self, request):
        order = Order.get_editable_order(request.user)
        order.close_order()
        return redirect(reverse('userprofile', kwargs={'pk': request.user.id}))


# review
class ReviewCreateView(CreateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'review_form.html'
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        form.instance.order_item_id = self.kwargs.get('order_item_id')
        return super().form_valid(form)


class ReviewEditView(UpdateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'review_form.html'
    success_url = reverse_lazy('categories')


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = reverse_lazy('categories')
