from django.db import models

class Move(models.Model):
    name = models.CharField(max_length=255)
    damage = models.IntegerField(default=0)

    def __str__(self):
        return self.name
