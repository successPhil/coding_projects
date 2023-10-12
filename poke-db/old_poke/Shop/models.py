from django.db import models
from Items.models import Item

class Shop(models.Model):
    items = models.ManyToManyField(Item, related_name='shop_items')

    def __str__(self):
        return f'Shop #{self.id}'
