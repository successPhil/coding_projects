from django.contrib.auth.models import User
from django.db import models
from pokemon.models import Pokemon
from Items.models import Item
from Shop.models import Shop
from Shop.views import create_initial_shop
import random

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=500)
    trainer_power = models.IntegerField(default=15)
    pokemon = models.ManyToManyField(Pokemon, related_name='trainer_pokemon', blank=True, default=None)
    items = models.ManyToManyField(Item, related_name='trainers_items', default=None, blank=True)
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, default=None, null=True)
    enemy_pokemon = models.ManyToManyField(Pokemon, related_name='enemy_pokemon', blank=True, default=None)

#Setting up initial shop for Trainer
    def set_initial_shop(self):
        if self.shop is None:
            initial_shop = create_initial_shop()  # Call the method to create initial shop
            self.shop = initial_shop
            self.save()

    def make_money(self):
        self.money += 1000
    
    def list_items(self):
        items = self.items.all()
        items_list = []
        for item in items:
            item_details = {
                "name": item.name,
                "value": item.value,
                "stat_boost": item.stat_boost,
                "item_class": item.item_class,
                "quantity": item.quantity
            }
            items_list.append(item_details)
        return items_list
    
    def list_shop(self):
        items = self.shop.items.all()
        items_list = []
        for item in items:
            item_details = {
                "name": item.name,
                "value": item.value,
                "stat_boost": item.stat_boost,
                "item_class": item.item_class,
                "quantity": item.quantity
            }
            items_list.append(item_details)

        return items_list
    
    def sell_item(self, item, qty=1):
        try:
            shop_item = self.shop.items.get(name=item.name)
        except Item.DoesNotExist:
            #If item does not exist in store create it
            shop_item = Item.objects.create(
                name=item.name,
                value=item.value,
                stat_boost=item.stat_boost,
                item_class=item.item_class,
                quantity=0
            )
            self.shop.items.add(shop_item) #add shop_item to shop items

        if item.quantity >= qty > 0:
            sale_price = item.value * qty
            self.money += sale_price
            item.decrement_quantity(qty) #Decrease trainer item quantity
            shop_item.increment_quantity(qty) #Increase shop item quantity
            self.save()

        #     print(f'Sold {qty} {item.name}(s) for {sale_price} money')
        # else:
        #     print(f'Not enough {item.name} to sell')

    def buy_item(self, item, qty=1):
        try:
            trainer_item = self.items.get(name=item.name)
        except Item.DoesNotExist:
            trainer_item = Item.objects.create(
                name=item.name,
                value=item.value,
                stat_boost=item.stat_boost,
                item_class=item.item_class,
                quantity=0
            )
            self.items.add(trainer_item)
            self.save()
        if item.quantity >= qty > 0:
            sale_price = item.value * qty
            if self.money >= sale_price:
                self.money -= sale_price
                trainer_item.increment_quantity(qty)
                item.decrement_quantity(qty)
                item.save()
                self.save()
        #         print(f'Purchased {qty} {item.name}(s) for {sale_price} money')
        #     else:
        #         print(f'Not enough money to purchase {qty} {item.name}')
        # else:
        #     print(f'Not enough {item.name} in stock')

    def use_item(self, item, pokemon, qty=1):
        item_map = {
            'health': pokemon.increase_health,
            'maxhealth': pokemon.increase_max_health,
            'damage': pokemon.increase_power,
            'defense': pokemon.increase_defense
        }

        item_function = item_map.get(item.item_class)
        if item_function:
            item_function(item.stat_boost * qty)
            item.decrement_quantity(qty)


    def add_pokemon(self, pokemon):
        self.pokemon.add(pokemon)
    
    def remove_pokemon(self, pokemon):
        self.pokemon.remove(pokemon)

    def first_pokemon(self):
        if not self.pokemon.exists():
            all_pokemon = Pokemon.objects.all()
            pokemon_choice = random.choice(all_pokemon)
            self.add_pokemon(pokemon_choice)
    
    def get_enemy_pokemon(self):
        if not self.enemy_pokemon.exists():
            all_pokemon = Pokemon.objects.all()
            pokemon_choice = random.choice(all_pokemon)
            self.enemy_pokemon.add(pokemon_choice)
                    



