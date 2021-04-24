from datetime import datetime

from django.conf import settings
from django.db import models


class Reviews(models.Model):
    ON_MODERATION = 'MOD'
    PUBLISHED = 'PUB'
    REJECTED = 'REJ'
    STATUS_CHOICES = [
        (ON_MODERATION, 'на модерации'),
        (PUBLISHED, 'опубликован'),
        (REJECTED, 'отклонен'),
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    published_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if self.status == self.PUBLISHED and not self.published_at:
            self.published_at = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.text[:50]}'
