from django.db import models
from moves.models import Move


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    front_image_url = models.URLField()
    back_image_url = models.URLField()
    health = models.IntegerField(default=45)
    max_health = models.IntegerField(default=45)
    moves = models.ManyToManyField(Move, related_name='pokemon_moves', blank=True)
    # Add more fields as needed

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.save()
