from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView

from BookShop.aws import conf
from Bookies.models import Book, Review

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),
         {'books': Book.objects.all(),
          'newest_book': Book.objects.all().order_by('-id')[:4],
          'newest_review': Review.objects.all().order_by('-id')[:4]
          },
         name="index"),
    path('admin/', admin.site.urls, name='admin'),
    path("accounts/", include("accounts.urls")),
    path('bookies/', include('Bookies.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(conf.MEDIA_URL, document_root=conf.MEDIA_ROOT)
