from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Reviews(models.Model):

    class Status(models.TextChoices):
        ON_MODERATION = 'MOD', _('на модерации')
        PUBLISHED = 'PUB', _('опубликован')
        REJECTED = 'REJ', _('отклонен')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    published_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=3, choices=Status.choices)

    def save(self, *args, **kwargs):
        if self.status == self.Status.PUBLISHED and not self.published_at:
            self.published_at = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.text[:50]}'
