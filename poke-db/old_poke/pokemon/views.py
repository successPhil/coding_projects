import requests
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon, Move
from .serializers import PokemonSerializer

class PokemonAPIView(APIView):
    def get(self, request):
        try:
            # 1. Fetch Pokémon Names
            names = self.fetch_pokemon_names()
            
            # 2. Fetch Generation 1 Moves
            moves = self.fetch_gen1_moves()
            
            # 3. Iterate Over Pokémon Names and Fetch Detailed Data
            details = self.fetch_pokemon_details(names)
            
            # 4. Process and Serialize the Data
            processed_data = self.process_pokemon_data(details, moves)
            
            return Response(processed_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def fetch_pokemon_names(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Replace with the correct URL
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [pokemon["name"] for pokemon in data["results"]]
        else:
            raise Exception("Failed to fetch Pokémon names")

    def fetch_gen1_moves(self):
        url = "https://pokeapi.co/api/v2/generation/1"  # URL to fetch Generation 1 moves
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            moves = [move_data["name"] for move_data in data["moves"]]
            return moves
        else:
            raise Exception("Failed to fetch Generation 1 moves")

    def fetch_pokemon_details(self, names):
        details = []
        for name in names:
            # Make a separate API request for each Pokémon name
            url = f"https://pokeapi.co/api/v2/pokemon/{name}"  # Replace with the correct URL
            response = requests.get(url)
            if response.status_code == 200:
                pokemon_data = response.json()
                # Extract relevant data and create a dictionary
                pokemon_details = {
                    "name": pokemon_data["name"],
                    "type": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
                    "front_image_url": pokemon_data["sprites"]["front_default"],
                    "back_image_url": pokemon_data["sprites"]["back_default"],
                }
                details.append(pokemon_details)
            else:
                raise Exception(f"Failed to fetch data for Pokémon: {name}")
        return details

    def process_pokemon_data(self, details, moves):
        processed_data = []
        for detail in details:
            # Customize and process the data here as needed
            name = detail["name"]
            type_str = ", ".join(detail["type"])
            front_image_url = detail["front_image_url"]
            back_image_url = detail["back_image_url"]
            level = self.calculate_level()
            experience, total_experience = self.calculate_experience(level)
            health = self.calculate_health(level)
            pokemon_moves = self.get_random_moves(moves)

            processed_detail = {
                "name": name,
                "type": type_str,
                "front_image_url": front_image_url,
                "back_image_url": back_image_url,
                "health": health,
                "level": level,
                "experience": f"{experience}/{total_experience}",
                "moves": pokemon_moves,
            }
            processed_data.append(processed_detail)
        return processed_data

    def calculate_health(self, level):
        base_health = 50  # Adjust the base health value as needed
        health = base_health + (level * 10)  # Increase health by 10 for each level
        return health

    def calculate_level(self):
        return random.randint(3, 10)  # Random level between 1 and 100

    def calculate_experience(self, level):
        # Calculate total experience needed for the current level and the next level
        current_experience = random.randint(0, 1000)  # Random current experience
        total_experience = level * 45  # Adjust the formula as needed
        return current_experience, total_experience

    def get_random_moves(self, moves):
        num_moves = 4  # Number of moves a Pokémon can have
        random_moves = random.sample(moves, num_moves)  # Select random moves from the list
        moves_with_damage = [{"name": move, "damage": random.randint(2, 10)} for move in random_moves]
        return moves_with_damage
