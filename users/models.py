from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    mobile = models.IntegerField(max_length=12)
    address = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user)

