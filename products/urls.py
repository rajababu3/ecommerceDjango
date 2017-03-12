from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^products/$', views.all, name='products'),
    #getting unique product link with slug
    url(r'^products/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.single,name='product_detail'),
    #url for search
    url(r'^s/$', views.search, name = 'search'),
]
