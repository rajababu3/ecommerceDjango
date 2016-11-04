from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout/$', views.checkout, name="checkout" ),
    url(r'^orders/success$', views.success, name="success" ),
    url(r'^orders/userOrder/(?P<user>\w+)/$', views.user_order, name="userOrder" ),

]