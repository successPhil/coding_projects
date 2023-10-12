from Shop.models import Shop
from Items.models import Item

def create_initial_shop():
    # Create Shop
    shop = Shop.objects.create()

    # Define initial items
    item_data = [
        {"name": "HP Potion", "value": 25, "stat_boost": 50, "item_class": "health", "quantity": 50},
        {"name": "Super HP Potion", "value": 100, "stat_boost": 50, "item_class": "health", "quantity": 35},
        {"name": "Warm Home Cooked Meal", "value": 200, "stat_boost": 100, "item_class": "health", "quantity": 10},
    ]

    # Create and associate items with the shop
    for item_info in item_data:
        item = Item.objects.create(
            name=item_info["name"],
            value=item_info["value"],
            stat_boost=item_info["stat_boost"],
            item_class=item_info["item_class"],
            quantity=item_info["quantity"]
        )

        shop.items.add(item)

    return shop