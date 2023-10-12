from rest_framework import serializers
from .models import Pokemon, Move

class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.PrimaryKeyRelatedField(many=True, queryset=Move.objects.all())

    class Meta:
        model = Pokemon
        fields = '__all__'
