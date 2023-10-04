from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
# VISTA BASADA EN CLASES
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
# Import de model 
from .models import Pokemon

# Vista basada en CLASES
# Read
class PokemonList(ListView): # pokemon_form.html
    model = Pokemon
    
# Create
class PokemonCreate(LoginRequiredMixin, CreateView): # Usan el mismo HTML pokemon_form.html
    model = Pokemon
    form_class = (
        PokemonForm
    )
    success_url = '/pokemons/pokemonList'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user  # Asigna el usuario actual como propietario
        return super().form_valid(form)
    
# Update
class PokemonUpdate(LoginRequiredMixin, UpdateView): # Usan el mismo HTML pokemon_form.html
    model = Pokemon
    form_class = (
        PokemonForm
    )
    success_url = '/pokemons/pokemonList'
    
# Delete 
class PokemonDelete(LoginRequiredMixin, DeleteView): # pokemon_confirm_delete.html
    model = Pokemon
    success_url = '/pokemons/pokemonList'
    
# Detail View
class PokemonDetail(DetailView): # <nombre_del_modelo>_detail.html
    model = Pokemon