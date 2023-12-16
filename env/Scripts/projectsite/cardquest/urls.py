from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name="trainer-list"),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', TrainerDeleteView.as_view(), name='trainer-delete'),

    path('pokemoncard_list', PokemonCardListView.as_view(), name='pokemoncard'),
    path('pokemon_list/add', PokemonCreateView.as_view(), name='pokemoncard-add'),
    path('pokemon_list/<pk>', PokemonUpdateView.as_view(), name='pokemoncard-update'),
    path('pokemon_list/<pk>/delete', PokemonDeleteView.as_view(), name='pokemoncard-del'),

    path('collection_list', CollectionList.as_view(), name='collection-list'),
    path('collection_list/add', CollectionCreateView.as_view(), name='collection-add'),
    path('collection_list/<pk>', CollectionUpdateView.as_view(), name="collection-update"),
    path('collection_list/<pk>/delete', CollectionDeleteView.as_view(), name='collection-del'),
]
