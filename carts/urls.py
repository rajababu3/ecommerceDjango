from django.conf.urls import url
import orders
from orders import views
from . import  views
urlpatterns = [
    url(r'^cart/$', views.view, name = 'cart'),
    url(r'^cart/(?P<id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^checkout/$', orders.views.checkout, name="checkout"),

]