from django.urls import path

from . import views

urlpatterns = [

path('pokemon/', views.PokemonAPIView.as_view(), name='pokemon-list'),

]