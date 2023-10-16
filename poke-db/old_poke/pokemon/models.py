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
    defense = models.IntegerField(default=10)
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

    def increase_max_health(self, amount):
        self.max_health += amount
        self.save()

    def increase_power(self, amount):
        self.power += amount
        self.save()

    def increase_defense(self, amount):
        self.defense += amount
    
    def level_up(self):
        additional_XP = int((self.totalXP/20) + self.level ** 1.3)
        self.level += 1
        self.totalXP+= additional_XP
        self.increase_max_health(25)
        self.increase_health(25)
        self.increase_power(6)
        self.increase_defense(10)
        self.save()

    def gain_experience(self, experience):
        self.experience += experience
        # Check if the Pokémon has gained enough experience to level up
        while self.experience >= self.totalXP:
            self.experience -= self.totalXP  # Deduct totalXP for leveling up
            self.level_up()
        # Save any remaining experience
        self.save()
