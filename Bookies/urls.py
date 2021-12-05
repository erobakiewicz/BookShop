from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from BookShop.aws import conf
from Bookies import views
from Bookies.views import BooksListView, AuthorsTemplateView, \
    CategoryTemplateView, BookDetailView, \
    AuthorDetailView, CategoryDetailView, BookEditView, BookCreateView, \
    BookDeleteView, AuthorCreateView, \
    AuthorEditView, AuthorDeleteView, CategoryCreateView, CategoryEditView, \
    CategoryDeleteView, AddOrderItemView, \
    CartView, Checkout, ReviewCreateView, ReviewEditView, ReviewDeleteView, \
    DeleteOrderItemView

handler404 = 'Bookies.views.handler404'

urlpatterns = [
    path('all/', BooksListView.as_view(), name='allbooks'),
    path('all/<slug:slug>/', BookDetailView.as_view(), name='bookdetails'),
    path('all/create/', BookCreateView.as_view(), name='createbook'),
    path('all/edit/<int:pk>', BookEditView.as_view(), name='editbook'),
    path('all/delete/<int:pk>', BookDeleteView.as_view(), name='deletebook'),

    path('authors/', AuthorsTemplateView.as_view(), name='authors'),
    path('authors/<slug:slug>/', AuthorDetailView.as_view(),
         name='authordetails'),
    path('authors/create/', AuthorCreateView.as_view(), name='createauthor'),
    path('authors/edit/<int:pk>', AuthorEditView.as_view(), name='editauthor'),
    path('authors/delete/<int:pk>', AuthorDeleteView.as_view(),
         name='deleteauthor'),

    path('categories/', CategoryTemplateView.as_view(), name='categories'),
    path('categories/<slug:slug>', CategoryDetailView.as_view(),
         name='categorydetials'),
    path('categories/create/', CategoryCreateView.as_view(),
         name='createcategory'),
    path('categories/edit/<int:pk>', CategoryEditView.as_view(),
         name='editcategory'),
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view(),
         name='deletecategory'),

    path('review/<int:order_item_id>/create/', ReviewCreateView.as_view(),
         name='createreview'),
    path('review/edit/<int:pk>', ReviewEditView.as_view(), name='editreview'),
    path('review/delete/<int:pk>', ReviewDeleteView.as_view(),
         name='deletereview'),

    path('add_item/<int:book_id>/', AddOrderItemView.as_view(),
         name='add_order_view'),
    path('cart/delete/<int:pk>', DeleteOrderItemView.as_view(),
         name='deleteorderitem'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('checkout/', Checkout.as_view(), name='checkout'),

    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(conf.MEDIA_URL, document_root=conf.MEDIA_ROOT)
