from django.db import models
from moves.models import Move


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    front_image_url = models.URLField()
    back_image_url = models.URLField()
    health = models.IntegerField(default=75)
    max_health = models.IntegerField(default=75)
    power = models.IntegerField(default=15)
    moves = models.ManyToManyField(Move, related_name='pokemon_moves', blank=True)
    experience = models.IntegerField(default=0)
    totalXP = models.IntegerField(default=60)
    level = models.IntegerField(default=3)

    # Add more fields as needed

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.save()

    def increase_health(self, amount):
        missing_health = self.max_health - self.health
        if missing_health <= amount:
            self.health += missing_health
        else:
            self.health += amount
