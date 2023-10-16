from django.urls import path, register_converter
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignupView, TrainerPokemonView, FirstPokemonView, EnemyPokemonView, BattleResultsView
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    path('get-token', obtain_auth_token),
    path('signup', SignupView.as_view()),
    path('first-poke', FirstPokemonView.as_view()),
    path('enemy-poke', EnemyPokemonView.as_view()),
    path('battleResults', BattleResultsView.as_view()),
    path('pokemon', TrainerPokemonView.as_view()),
    path('pokemon/<int_or_str:id>/', TrainerPokemonView.as_view())
]