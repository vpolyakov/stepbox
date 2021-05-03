from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=150, blank=True)

    def cart(self):
        from carts.models import Cart
        return Cart.objects.get_or_create(user=self)[0]

    def __str__(self):
        return '%s' % self.username
