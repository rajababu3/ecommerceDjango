from django.contrib import admin

from .models import UserProfile,UserOrder

admin.site.register(UserProfile)
admin.site.register(UserOrder)