"""BookShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView

from BookShop.aws import conf
from Bookies.models import Book, Review

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), {'books': Book.objects.all(),
                                                                'newest_book': Book.objects.all().order_by('-id')[:4],
                                                                'newest_review': Review.objects.all().order_by('-id')[
                                                                                 :4]
                                                                },
         name="index"),
    path('admin/', admin.site.urls, name='admin'),
    path("accounts/", include("accounts.urls")),
    path('bookies/', include('Bookies.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(conf.MEDIA_URL, document_root=conf.MEDIA_ROOT)
