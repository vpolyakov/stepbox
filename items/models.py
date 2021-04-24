from django.db import models

from stepbox.settings import MEDIA_ITEM_IMAGE_DIR


class Item(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to=MEDIA_ITEM_IMAGE_DIR + '/', default='150x150.gif')
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '%s' % self.title
