from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from Trainer.serializers import SignupSerializer, TrainerSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Trainer.models import Trainer
from Items.models import Item
from Shop.views import create_initial_shop
from pokemon.serializers import PokemonSerializer

# handles request and parses body for username and password
class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            #create_user is special method. must be used to create user
            user = User.objects.create_user(username=username, password=password)
            trainer = Trainer.objects.create(user=user, money=500, trainer_power=15)

            initial_shop = create_initial_shop()
            trainer.shop = initial_shop

            # Save the trainer to associate them with the shop
            trainer.save()

            # Add 10 potions to the trainer
            potion_data = {"name": "HP Potion", "value": 25, "stat_boost": 50, "item_class": "health", "quantity": 10}

            item = Item.objects.create(
                name=potion_data["name"],
                value=potion_data["value"],
                stat_boost=potion_data["stat_boost"],
                item_class=potion_data["item_class"],
                quantity=potion_data["quantity"]
            )

            trainer.items.add(item)

            trainer_serializer = TrainerSerializer(trainer)

            return Response({
                'user_id': user.id,
                'trainer': trainer_serializer.data,
            })
    
class TrainerPokemonView(APIView):
    def get(self, request, id=None):
        user = request.user

        try:
            trainer = Trainer.objects.get(user=user)  # Ensure trainer is retrieved correctly

            if id is not None:
                if isinstance(id, int):
                    trainer_poke = trainer.pokemon.get(id=id)
                elif isinstance(id, str):
                    trainer_poke = trainer.pokemon.get(name=id)
                else:
                    raise ValueError("Invalid ID or name")
                serializer = PokemonSerializer(trainer_poke)
            else:
                all_pokemon = trainer.pokemon.all()
                serializer = PokemonSerializer(all_pokemon, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Trainer.DoesNotExist:
            return Response({'message': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)