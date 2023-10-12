from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from Trainer.serializers import SignupSerializer, TrainerSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Trainer.models import Trainer
from Items.models import Item
from Shop.views import create_initial_shop

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