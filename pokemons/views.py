from django.shortcuts import render, HttpResponse
from .forms import *
# VISTA BASADA EN CLASES
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
# Import de model 
from .models import Pokemon

# Create your views here.
# Vista de Busquedas
def pokemon_search_result(request):
    if request.GET['pokemon']:
        name = request.GET['pokemon']
        pokemon = Pokemon.objects.filter(name__icontains=name)
        return render(request, 'pokemons/search_pokemon.html', { 'name': name, 'pokemon': pokemon})
    else:
        advice = f'No se enviaron datos!'
        
    return HttpResponse(advice)

# Vista basada en CLASES
# Read
class PokemonList(ListView): # pokemon_form.html
    model = Pokemon
    # template_name = 'myApp/pokemon_list.html' - SE DETALLA EL NOMBRE DEL TEMPLATE A USAR SI NO ES POR DEFECTO
    
# Create 
class PokemonCreate(CreateView): # Usan el mismo HTML pokemon_form.html
    model = Pokemon
    form_class = (
        PokemonForm
    )
    success_url = '/pokemonList'
    
# Update
class PokemonUpdate(UpdateView): # Usan el mismo HTML pokemon_form.html
    model = Pokemon
    form_class = (
        PokemonForm
    )
    success_url = '/pokemonList'
    
# Delete 
class PokemonDelete(DeleteView): # pokemon_confirm_delete.html
    model = Pokemon
    success_url = '/pokemonList'
    
# Detail View
class PokemonDetail(DetailView): # <nombre_del_modelo>_detail.html
    model = Pokemon