from Shop.models import Shop
from Items.models import Item
import json

def create_initial_shop():
    # Create Shop
    shop = Shop.objects.create()

    # Define initial items
    # item_data = [
    #     {"name": "HP Potion", "value": 25, "stat_boost": 50, "item_class": "health", "quantity": 900},
    #     {"name": "Super HP Potion", "value": 400, "stat_boost": 800, "item_class": "health", "quantity": 900},
    #     {"name": "Warm Home Cooked Meal", "value": 200, "stat_boost": 600, "item_class": "health", "quantity": 300},
    #     {"name": "Ember Essence", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Blazing Ember", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Inferno Elixir", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Flame Guard", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Refreshing Mist", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Aqua Crystal", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Tidal Surge", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Aqua Shield", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Photosynthesis Potion", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Verdant Bloom", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Thorny Vines", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Leafy Barrier", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Electroshock Serum", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Thunderbolt Charger", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Voltage Amplifier", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Shock Absorber", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Earthquake Tonic", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Terra Infusion", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Rocky Rampart", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Earthen Barrier", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Metal Alloy Infusion", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Ironclad Plate", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Steel Surge", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Adamantium Shield", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Psychic Resonance Tincture", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Mindsoothe Elixir", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Psionic Focus", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Mental Ward", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Chitin Carapace Salve", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Insectile Nectar", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Swarm Surge", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Bug Repellent Barrier", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Fae Essence Elixir", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Enchanted Blossom", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Pixie Dust Gust", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Moonlit Veil", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Soaring Wind Tonic", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Aerial Draft Elixir", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Skyward Strike", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Feathered Gale Guard", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Ghostly Haze", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Spectral Essence Elixir", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Haunting Wail", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Ethereal Cloak", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Venombane Elixir", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Toxic Venom Vial", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Venomous Strike", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Poison Veil", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Combatant's Elixir", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Brawler's Brew", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Pugilist's Potion", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Martial Draught", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Earthward Elixir", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Stoneshield Tonic", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Bedrock Brew", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Granite Guard", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Glacial Draught", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Frostbound Elixir", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Polar Respite", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Icicle Infusion", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Wyrmward Potion", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Dragonfire Elixir", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Drakon's Draught", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Serpent's Serum", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    #     {"name": "Chocolate Cheesecake", "value": 1500, "stat_boost": 3000, "item_class": "health", "quantity": 300},
    #     {"name": "Protein Shake", "value": 2000, "stat_boost": 75, "item_class": "maxhealth", "quantity": 20},
    #     {"name": "Knuckle Sandwich", "value": 450, "stat_boost": 4, "item_class": "damage", "quantity": 10},
    #     {"name": "Honorable Cookie", "value": 350, "stat_boost": 3, "item_class": "defense", "quantity": 30},
    # ]

    # Create and associate items with the shop
    with open("Shop/initial_shop_items/initial_shop_items.json") as f:
        item_data = json.load(f)


    for item_info in item_data:
        item = Item.objects.create(
            name=item_info["name"],
            value=item_info["value"],
            stat_boost=item_info["stat_boost"],
            item_class=item_info["item_class"],
            item_type=item_info["item_type"],
            quantity=item_info["quantity"]
        )

        shop.items.add(item)

    return shop