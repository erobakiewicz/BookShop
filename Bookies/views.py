from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, \
    DeleteView, TemplateView

from Bookies.constants import OrderStatuses
from Bookies.models import Book, Author, Category, Review, Order, OrderItem

# book views
from Bookies.tasks import order_created


class BooksListView(ListView):
    model = Book
    paginate_by = 4
    ordering = ['-id']
    template_name = 'all_books.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['query'] = self.request.GET.get('q', '')
        return ctx

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | Q(
                    author__name__icontains=query) | Q(
                    description__icontains=query))
        else:
            return Book.objects.all()


# detail view
class BookDetailView(DetailView):
    model = Book
    template_name = "book_details.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'reviews': Review.objects.filter(
                order_item__book_id=self.kwargs.get('pk'))},
        )
        return context


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'available', 'img',
              'category']
    template_name = 'book_form.html'
    success_url = reverse_lazy('allbooks')


class BookEditView(UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'price', 'available', 'img',
              'category']
    template_name = 'book_form.html'
    success_url = reverse_lazy('allbooks')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('allbooks')


# author views

class AuthorsTemplateView(ListView):
    model = Author
    paginate_by = 4
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
    paginate_by = 4
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'authors': Category.objects.all()})
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Category.objects.filter(name__icontains=query)
        else:
            return Category.objects.all()


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
        try:
            OrderItem.objects.get(
                book_id=self.kwargs.get('book_id'),
                order=order
            )
        except OrderItem.DoesNotExist:
            OrderItem.objects.create(
                book_id=self.kwargs.get('book_id'),
                order=order)
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class Checkout(View):
    def post(self, request):
        order = Order.get_editable_order(request.user)
        order.close_order()
        order_created.delay(order.id)
        return redirect(reverse('userprofile', kwargs={'pk': request.user.id}))


# review

class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'review_form.html'
    success_url = reverse_lazy('userprofile')

    def test_func(self):
        order_item = get_object_or_404(
            OrderItem,
            pk=self.kwargs.get('order_item_id')
        )
        if order_item.order.user != self.request.user:
            return False
        elif order_item.order.status != OrderStatuses.COMLETED:
            return False
        return True

    def form_valid(self, form):
        try:
            form.instance.order_item_id = self.kwargs.get('order_item_id')
            return super().form_valid(form)
        except ValueError:
            raise Exception("You wrote it already")


class ReviewEditView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'review_form.html'
    success_url = reverse_lazy('categories')


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = reverse_lazy('categories')


def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response
