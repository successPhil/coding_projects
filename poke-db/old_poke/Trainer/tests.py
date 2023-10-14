from django.test import TestCase
from django.contrib.auth.models import User
from Trainer.models import Trainer
from Items.models import Item
from pokemon.models import Pokemon

from rest_framework.test import APITestCase

class SignupViewTest(APITestCase):
    def setUp(self):
        url = '/login/signup'  #url for signup view
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        #use client to make post to url with data
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201) #check response of post
        self.trainer = Trainer.objects.get(user__username='testuser') #store trainer for testing
        self.pokemon = Pokemon.objects.create(name='charmander',types='fire', front_image_url='something.jpeg', back_image_url='somethingelse.jpeg')
        self.store_item = self.trainer.shop.items.get(name='Warm Home Cooked Meal') #Item from store
        self.default_item = self.trainer.shop.items.get(name='HP Potion') #Initial Trainer Item
        self.trainer_item = self.trainer.items.get(name='HP Potion')
        self.initial_item_qty = self.trainer_item.quantity #Starting item quantity (HP Potion)
        self.initial_money = self.trainer.money #starting money
        self.assertIsNotNone(self.store_item) #make sure store item exists
        self.assertIsNotNone(self.default_item) #make sure default item exists
        self.initial_pokemon_count = self.trainer.pokemon.count() #initial pokemon count
        self.initial_enemy_count = self.trainer.enemy_pokemon.count() #initial enemy pokemon count

    def test_signup_view(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Trainer.objects.count(), 1)

    def test_trainer_creation(self):
        self.assertEqual(User.objects.count(), 1) #Check User is created
        self.assertEqual(Trainer.objects.count(), 1) #Check Trainer is created
        # Check if the Trainer has the correct initial shop and items
        self.assertIsNotNone(self.trainer.shop) #Shop exists
        self.assertEqual(self.trainer.items.count(), 1) #Initial items exist

    def test_make_money(self):
        self.trainer.make_money()
        final_money = self.trainer.money
        self.assertEqual(final_money-self.initial_money, 1000)

    def test_list_items(self):
        trainer_items = self.trainer.items.all()
        self.assertEqual(len(trainer_items), self.trainer.items.count())

    def test_buy_existing_item_default_qty(self):
        initial_store_qty = self.default_item.quantity
        initial_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.trainer.buy_item(self.default_item)
        final_money = self.trainer.money
        final_store_qty = self.default_item.quantity
        final_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        
        self.assertEqual(self.initial_money-final_money, self.default_item.value) #Check trainer money
        self.assertEqual(final_store_qty + 1, initial_store_qty) #Check store qty
        self.assertEqual(final_trainer_qty - 1, initial_trainer_qty) #Check trainer qty
    
    def test_buy_existing_item_valid_qty(self):
        initial_store_qty = self.default_item.quantity
        initial_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.trainer.buy_item(self.default_item, 4)
        final_money = self.trainer.money
        final_store_qty = self.default_item.quantity
        final_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.assertEqual(self.initial_money-final_money, self.default_item.value * 4)
        self.assertEqual(final_store_qty + 4, initial_store_qty)
        self.assertEqual(final_trainer_qty - 4, initial_trainer_qty)

    def test_buy_existing_item_invalid_qty(self):
        initial_store_qty = self.default_item.quantity
        initial_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.trainer.buy_item(self.default_item, 450)
        final_money = self.trainer.money
        final_store_qty = self.default_item.quantity
        final_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.assertEqual(self.initial_money, final_money)
        self.assertEqual(initial_store_qty, final_store_qty)
        self.assertEqual(initial_trainer_qty, final_trainer_qty)

    def test_buy_new_item_default_qty(self):
        initial_store_qty = self.store_item.quantity
        initial_trainer_qty = 0
        self.trainer.buy_item(self.store_item)
        final_money = self.trainer.money
        final_store_qty = self.store_item.quantity
        final_trainer_qty = self.trainer.items.get(name='Warm Home Cooked Meal').quantity
        self.assertEqual(self.initial_money-final_money, self.store_item.value)
        self.assertEqual(final_store_qty + 1, initial_store_qty)
        self.assertEqual(final_trainer_qty - 1, initial_trainer_qty)

    def test_buy_new_item_valid_qty(self):
        initial_store_qty = self.store_item.quantity
        initial_trainer_qty = 0
        self.trainer.buy_item(self.store_item, 2)
        final_money = self.trainer.money
        final_store_qty = self.store_item.quantity
        final_trainer_qty = self.trainer.items.get(name='Warm Home Cooked Meal').quantity
        self.assertEqual(self.initial_money-final_money, self.store_item.value * 2)
        self.assertEqual(final_store_qty + 2, initial_store_qty)
        self.assertEqual(final_trainer_qty - 2, initial_trainer_qty)

    def test_buy_new_item_invalid_qty(self):
        initial_store_qty = self.store_item.quantity
        initial_trainer_qty = 0
        self.trainer.buy_item(self.store_item, 200)
        final_money = self.trainer.money
        final_store_qty = self.store_item.quantity
        final_trainer_qty = self.trainer.items.get(name='Warm Home Cooked Meal').quantity
        self.assertEqual(self.initial_money, final_money)
        self.assertEqual(final_store_qty, initial_store_qty)
        self.assertEqual(final_trainer_qty, initial_trainer_qty)

    def test_sell_item_default_qty(self):
        initial_trainer_qty = self.trainer_item.quantity    
        initial_store_qty = self.trainer.shop.items.get(name='HP Potion').quantity
        self.trainer.sell_item(self.trainer_item)
        final_money = self.trainer.money
        final_trainer_qty = self.trainer_item.quantity
        final_store_qty = self.trainer.shop.items.get(name='HP Potion').quantity
        self.assertEqual(final_money-self.initial_money, self.trainer_item.value)
        self.assertEqual(final_trainer_qty + 1, initial_trainer_qty)
        self.assertEqual(final_store_qty - 1, initial_store_qty)

    def test_sell_item_valid_qty(self):
        initial_trainer_qty = self.trainer_item.quantity    
        initial_store_qty = self.trainer.shop.items.get(name='HP Potion').quantity
        self.trainer.sell_item(self.trainer_item, 3)
        final_money = self.trainer.money
        final_trainer_qty = self.trainer_item.quantity
        final_store_qty = self.trainer.shop.items.get(name='HP Potion').quantity
        self.assertEqual(final_money-self.initial_money, self.trainer_item.value * 3)
        self.assertEqual(final_trainer_qty + 3, initial_trainer_qty)
        self.assertEqual(final_store_qty - 3, initial_store_qty)

    def test_sell_item_invalid_qty(self):
        initial_trainer_qty = self.trainer_item.quantity    
        initial_store_qty = self.trainer.shop.items.get(name='HP Potion').quantity
        self.trainer.sell_item(self.trainer_item, 999)
        final_money = self.trainer.money
        final_trainer_qty = self.trainer_item.quantity
        final_store_qty = self.trainer.shop.items.get(name='HP Potion').quantity
        self.assertEqual(final_money, self.initial_money)
        self.assertEqual(final_trainer_qty, initial_trainer_qty)
        self.assertEqual(final_store_qty, initial_store_qty)

    def test_use_item_health_default_qty(self):
        self.trainer.first_pokemon()

        pokemon = self.trainer.pokemon.get(name='charmander')
        pokemon_initial_health = pokemon.health
        pokemon.decrease_health(50)
        self.assertEqual(pokemon_initial_health, pokemon.health + 50)

        self.trainer.use_item(self.trainer_item, pokemon)
        pokemon_final_health = pokemon.health
        item_final_qty = self.trainer_item.quantity
        self.assertEqual(pokemon_initial_health, pokemon_final_health)
        self.assertEqual(item_final_qty + 1, self.initial_item_qty)

    def test_use_item_health_multiple_qty(self):
        self.trainer.first_pokemon()

        pokemon = self.trainer.pokemon.get(name='charmander')
        pokemon_initial_health = pokemon.health
        pokemon.decrease_health(60)
        self.assertEqual(pokemon_initial_health, pokemon.health + 60)

        self.trainer.use_item(self.trainer_item, pokemon, 2)
        pokemon_final_health = pokemon.health
        item_final_qty = self.trainer_item.quantity
        self.assertEqual(pokemon_initial_health, pokemon_final_health)
        self.assertEqual(item_final_qty + 2, self.initial_item_qty)

    def test_add_pokemon(self):
        self.trainer.add_pokemon(self.pokemon)
        self.assertEqual(self.trainer.pokemon.count() - 1, self.initial_pokemon_count)

    def test_add_multiple_pokemon(self):
        pokemon = Pokemon.objects.create(name='charmander',types='fire', front_image_url='something.jpeg', back_image_url='somethingelse.jpeg')
        self.trainer.add_pokemon(pokemon)
        pokemon = Pokemon.objects.create(name='bulbasaur',types='grass', front_image_url='something.jpeg', back_image_url='somethingelse.jpeg')
        self.trainer.add_pokemon(pokemon)
        pokemon = Pokemon.objects.create(name='squirtle',types='water', front_image_url='something.jpeg', back_image_url='somethingelse.jpeg')
        self.trainer.add_pokemon(pokemon)
        self.assertEqual(self.trainer.pokemon.count() -3, self.initial_pokemon_count)

    def test_add_remove_multiple_pokemon(self):
        pokemon = Pokemon.objects.create(name='charmander',types='fire', front_image_url='something.jpeg', back_image_url='somethingelse.jpeg')
        self.trainer.add_pokemon(pokemon)
        self.assertEqual(self.trainer.pokemon.count() -1, self.initial_pokemon_count)

        pokemon = Pokemon.objects.create(name='bulbasaur',types='grass', front_image_url='something.jpeg', back_image_url='somethingelse.jpeg')
        self.trainer.add_pokemon(pokemon)
        self.assertEqual(self.trainer.pokemon.count() -2, self.initial_pokemon_count)

        pokemon = Pokemon.objects.create(name='squirtle',types='water', front_image_url='something.jpeg', back_image_url='somethingelse.jpeg')
        self.trainer.add_pokemon(pokemon)
        self.assertEqual(self.trainer.pokemon.count() -3, self.initial_pokemon_count)

        pokemon = self.trainer.pokemon.get(name='bulbasaur')
        self.trainer.remove_pokemon(pokemon)
        self.assertEqual(self.trainer.pokemon.count() - 2, self.initial_pokemon_count)

        pokemon = self.trainer.pokemon.get(name='squirtle')
        self.trainer.remove_pokemon(pokemon)
        self.assertEqual(self.trainer.pokemon.count() - 1, self.initial_pokemon_count)

        pokemon = self.trainer.pokemon.get(name='charmander')
        self.trainer.remove_pokemon(pokemon)
        self.assertEqual(self.trainer.pokemon.count(), self.initial_pokemon_count)

    def test_first_pokemon(self):
        self.trainer.first_pokemon()
        self.assertEqual(self.trainer.pokemon.count() - 1, self.initial_pokemon_count)

    def test_enemy_pokemon(self):
        self.trainer.get_enemy_pokemon()
        self.assertEqual(self.trainer.enemy_pokemon.count() - 1, self.initial_enemy_count)



    







    
        




