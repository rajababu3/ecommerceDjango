from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^users/logout/$', views.logout_view, name='auth_logout'),
    url(r'^users/login/$', views.login_view, name='auth_login'),
]