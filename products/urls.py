from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^products/$', views.all, name='products'),
    #getting unique product link with slug
    url(r'^products/(?P<slug>[\w-]+)/$', views.single, name='single-product'),
    #url for search
    url(r'^s/$', views.search, name = 'search'),
]
