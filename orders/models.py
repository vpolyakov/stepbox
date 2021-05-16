from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from carts.models import Cart


class Order(models.Model):

    class Status(models.TextChoices):
        CREATED = 'created', _('создан')
        DELIVERED = 'delivered', _('доставлен')
        PROCESSED = 'processed', _('обработан')
        CANCELLED = 'cancelled', _('отменен')

    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    delivery_at = models.DateTimeField(null=True)
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=256)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=9, choices=Status.choices)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Заказ №{self.id} Общая стоимость: {self.total_cost}'
