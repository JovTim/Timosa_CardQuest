from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import PokemonCard, Trainer, Collection
from .forms import TrainerForm, CollectionForm, PokemonCardForm

from django.urls import reverse_lazy
import json

# Create your views here.
class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer-list'
    template_name = 'trainer.html'
    paginate_by = 5

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')

class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemoncards.html"
    paginate_by = 5
    json_file_patch = 'data/pokemon_data.json'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
    
    def get_pokemon_data(self):
        with open(self.json_file_patch, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])

class PokemonCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemoncard_add.html'
    success_url = reverse_lazy('pokemoncard')
class PokemonUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemoncard_edit.html'
    success_url = reverse_lazy('pokemoncard')

class PokemonDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemoncard_del.html'
    success_url = reverse_lazy('pokemoncard')
    

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 5

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_add.html'
    success_url = reverse_lazy('collection-list')


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_edit.html'
    success_url = reverse_lazy('collection-list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collections_del.html'
    success_url = reverse_lazy('collection-list')