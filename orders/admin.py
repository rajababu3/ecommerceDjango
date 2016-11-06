from django.contrib import admin

# Register your models here.
from .models import Order, Tracking

admin.site.register(Order)
admin.site.register(Tracking)