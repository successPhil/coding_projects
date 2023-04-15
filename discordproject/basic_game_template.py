import random
#Starting with basic test inventory
inventory = {
    'seeds': 0,
    'carrots': 0,
    'bread': 0,
    'berries': 0,
    'rice': 0,
    'beans': 0,
    'onions': 0,
    'turnips': 0,
    'bananas': 0,
    'apples': 0,
    'oranges': 0,
    'wood': 0,
    'XP': 0,
    'gathercoins': 0
}
prepared = {}
#Recipe
recipes = {
'carrotcake': {'carrots': 10, 'bread': 10, 'berries': 16},
'fruitbowl': {'bananas': 6, 'oranges': 4, 'apples': 2, 'berries': 10},
'basicmeal': {'rice': 50, 'beans': 25}
}
#Created function gather(inventory) that the user can select to 'gather'random things ##
def Gather(inventory):
    for item in inventory:
        inventory[item] = inventory[item] + random.randint(10,12)
        print(f'You found {inventory[item]} {item}')

#Created function Make(prepared, recipes) to make prepared items into their recipes
def Make(prepared, recipes):
   for recipe_name, recipe in recipes.items():
     if all(item in prepared and prepared[item] >= amount for item, amount in recipe.items()):
       inventory.setdefault(recipe_name, 0)
       for item, amount in recipe.items():
         if item in inventory:
            inventory[item] -= amount
         
         if item in prepared:
            prepared[item] -= amount
         
         inventory[recipe_name] += 1
         print(f'You made {recipe_name}')
     else: 
         print(f"You don't have enough ingredients to make anything")
    
#Created function prepare(inventory) that user can select to 'prepare' recipes
def Prep(inventory):
  prepared.clear()
 
  while True:
    item = input("Enter an item name to select (or 'done' to finish)")
    if item == 'done':
      break
    if item not in inventory:
      print(f'{item} not in inventory')
      continue
    amount = int(input(f"Enter the amount of {item} to select:"))
    if amount > inventory[item]:
      print(f"Not enough {item} in inventory")
      continue       
    prepared[item] = amount
    print(prepared)

  return prepared
 #Created function for selling; increasing gathercoin   
def Sell(inventory):
    prices = {
        'seeds': 1,
        'carrots': 2,
        'bread': 4,
        'berries': 1,
        'rice': 3,
        'beans': 2,
        'onions': 2,
        'turnips': 3,
        'bananas': 3,
        'apples': 2,
        'oranges': 2,
        'wood': 1
    }
    
    while True:
        item = input("Enter an item name to sell (or 'done' to finish)")
        if item == 'done':
            break
        if item not in inventory:
            print(f'{item} not in inventory')
            continue
        amount = int(input(f"Enter the amount of {item} to sell:"))
        if amount > inventory[item]:
            print(f"Not enough {item} in inventory")
            continue
        inventory[item] -= amount
        price = prices[item] * amount
        inventory['gathercoins'] += price
        print(f"You sold {amount} {item} for {price} gathercoins")
#Created shop to trade in with gathercoin
def Trade(inventory):
    prices = {
        'seeds': 5,
        'carrots': 10,
        'bread': 15,
        'berries': 7,
        'rice': 12,
        'beans': 9,
        'onions': 8,
        'turnips': 11,
        'bananas': 14,
        'apples': 13,
        'oranges': 16,
        'wood': 20,
        'gathercoins': 1
    }
    print("Available items and prices:")
    for item, price in prices.items():
        print(f"{item}: {price} gathercoins")

    item_to_buy = input("Which item do you want to buy? ")
    amount_to_buy = int(input(f"How many {item_to_buy} do you want to buy? "))
    cost = prices.get(item_to_buy, 0) * amount_to_buy

    if cost > inventory['gathercoins']:
        print("You don't have enough gathercoins to buy this item.")
    else:
        inventory['gathercoins'] -= cost
        inventory.setdefault(item_to_buy, 0)
        inventory[item_to_buy] += amount_to_buy
        print(f"You bought {amount_to_buy} {item_to_buy} for {cost} gathercoins.")

    
#Basic while loop to allow user to 'play', must be set true to allow users to call functions
playing = True;
while playing:
#Generic prompt for test purposes
   response = input('Gather or not!')
   if response == 'gather':
        Gather(inventory)
   elif response == 'prepare':
        Prep(inventory)
   elif response == 'make':
        Make(prepared, recipes)
   elif response == 'quit':
      playing = False
      break
   elif response == 'inventory':
      print(f'This is your inventory: {inventory}')
      print(f'This is your prepared: {prepared}')
   elif response == 'sell':
      Sell(inventory)
   elif response == 'trade':
      Trade(inventory)

