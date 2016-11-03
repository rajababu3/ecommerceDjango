from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^users/logout/$', views.logout_view, name='auth_logout'),
    url(r'^users/login/$', views.login_view, name='auth_login'),
    url(r'^users/register/$', views.registration_view, name='auth_register'),
    url(r'^users/contact/$', views.contact_view, name='contact'),
    url(r'^users/address/shipping/$', views.add_user_address, name='shipping_address'),
    url(r'^users/thankyou/$', views.thankyou_view, name='thankyou'),
]