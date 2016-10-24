from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from carts.models import Cart

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)

class Order(models.Model):
    #add user
    # address **
    user = models.ForeignKey(User, default=1, null=True, blank=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart)
    cart_total = models.DecimalField(decimal_places=2, max_digits=100, default=850, null=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

