"""readalways URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = "lend"

urlpatterns = [
    url(r'^$', views.home, name='lend_home'),    
    url(r'^add$', views.create_book, name='lend-book-add'),
    url(r'^(?P<book_id>[0-9]+)/delete_book/$', views.delete_book, name='lend-book-delete'),
    url(r'^(?P<book_id>[0-9]+)/update_book/$', views.update_book, name='lend-book-update'),
    url(r'^approve/(?P<req_id>[0-9]+)/$', views.approve, name='lend-approve'),
    url(r'^reject/(?P<req_id>[0-9]+)/$', views.reject, name='lend-reject'),
]
