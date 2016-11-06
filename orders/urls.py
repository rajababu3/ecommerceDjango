from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout/$', views.checkout, name="checkout" ),
    url(r'^orders/success$', views.success, name="success" ),
    url(r'^orders/orderProcess', views.orderProcess, name="orderProcess" ),
    url(r'^orders/userOrder/(?P<user>\w+)/$', views.user_order, name="userOrder" ),
    url(r'^orders/orderTracking/(?P<order_id>[\w-]+)/$', views.track, name="orderTracking" ),

]