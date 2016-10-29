from django.contrib import admin

from .models import UserProfile, UserOrder, UserContact

admin.site.register(UserProfile)
admin.site.register(UserOrder)
admin.site.register(UserContact)