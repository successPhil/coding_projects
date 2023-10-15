from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignupView, TrainerPokemonView

urlpatterns = [
    path('get-token', obtain_auth_token),
    path('signup', SignupView.as_view()),
    path('pokemon', TrainerPokemonView.as_view()),
]