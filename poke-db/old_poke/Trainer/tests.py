from django.test import TestCase
from django.contrib.auth.models import User
from Trainer.models import Trainer

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
        self.store_item = self.trainer.shop.items.get(name='Warm Home Cooked Meal') #Item from store
        self.default_item = self.trainer.shop.items.get(name='HP Potion') #Initial Trainer Item
        self.assertIsNotNone(self.store_item) #make sure store item exists
        self.assertIsNotNone(self.default_item) #make sure default item exists

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
        initial_money = self.trainer.money
        self.trainer.make_money()
        final_money = self.trainer.money
        self.assertEqual(final_money-initial_money, 1000)

    def test_list_items(self):
        trainer_items = self.trainer.items.all()
        self.assertEqual(len(trainer_items), self.trainer.items.count())

    def test_buy_existing_item_default_qty(self):
        initial_money = self.trainer.money
        initial_store_qty = self.default_item.quantity
        initial_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.trainer.buy_item(self.default_item)
        final_money = self.trainer.money
        final_store_qty = self.default_item.quantity
        final_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        
        self.assertEqual(initial_money-final_money, self.default_item.value) #Check trainer money
        self.assertEqual(final_store_qty + 1, initial_store_qty) #Check store qty
        self.assertEqual(final_trainer_qty - 1, initial_trainer_qty) #Check trainer qty
    
    def test_buy_existing_item_valid_qty(self):
        initial_money = self.trainer.money
        initial_store_qty = self.default_item.quantity
        initial_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.trainer.buy_item(self.default_item, 4)
        final_money = self.trainer.money
        final_store_qty = self.default_item.quantity
        final_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.assertEqual(initial_money-final_money, self.default_item.value * 4)
        self.assertEqual(final_store_qty + 4, initial_store_qty)
        self.assertEqual(final_trainer_qty - 4, initial_trainer_qty)

    def test_buy_existing_item_invalid_qty(self):
        initial_money = self.trainer.money
        initial_store_qty = self.default_item.quantity
        initial_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.trainer.buy_item(self.default_item, 450)
        final_money = self.trainer.money
        final_store_qty = self.default_item.quantity
        final_trainer_qty = self.trainer.items.get(name='HP Potion').quantity
        self.assertEqual(initial_money, final_money)
        self.assertEqual(initial_store_qty, final_store_qty)
        self.assertEqual(initial_trainer_qty, final_trainer_qty)

    def test_buy_new_item_default_qty(self):
        initial_money = self.trainer.money
        initial_store_qty = self.store_item.quantity
        initial_trainer_qty = 0
        self.trainer.buy_item(self.store_item)
        final_money = self.trainer.money
        final_store_qty = self.store_item.quantity
        final_trainer_qty = self.trainer.items.get(name='Warm Home Cooked Meal').quantity
        self.assertEqual(initial_money-final_money, self.store_item.value)
        self.assertEqual(final_store_qty + 1, initial_store_qty)
        self.assertEqual(final_trainer_qty - 1, initial_trainer_qty)

    def test_buy_new_item_valid_qty(self):
        initial_money = self.trainer.money
        initial_store_qty = self.store_item.quantity
        initial_trainer_qty = 0
        self.trainer.buy_item(self.store_item, 2)
        final_money = self.trainer.money
        final_store_qty = self.store_item.quantity
        final_trainer_qty = self.trainer.items.get(name='Warm Home Cooked Meal').quantity
        self.assertEqual(initial_money-final_money, self.store_item.value * 2)
        self.assertEqual(final_store_qty + 2, initial_store_qty)
        self.assertEqual(final_trainer_qty - 2, initial_trainer_qty)

    def test_buy_new_item_invalid_qty(self):
        initial_money = self.trainer.money
        initial_store_qty = self.store_item.quantity
        initial_trainer_qty = 0
        self.trainer.buy_item(self.store_item, 200)
        final_money = self.trainer.money
        final_store_qty = self.store_item.quantity
        final_trainer_qty = self.trainer.items.get(name='Warm Home Cooked Meal').quantity
        self.assertEqual(initial_money, final_money)
        self.assertEqual(final_store_qty, initial_store_qty)
        self.assertEqual(final_trainer_qty, initial_trainer_qty)





    
        




