from django.urls import path
from pokemons import views

urlpatterns = [
    
    path('result', views.pokemon_search_result, name='PokemonSearch'),
    # Vista Basada en CLASS 
    path('pokemonList/', views.PokemonList.as_view() , name='PokemonList'),
    path('pokemonCreate/', views.PokemonCreate.as_view() , name='PokemonCreate'),
    path('pokemonUpdate/<int:pk>', views.PokemonUpdate.as_view() , name='PokemonUpdate'),
    path('pokemonDelete/<int:pk>', views.PokemonDelete.as_view() , name='PokemonDelete'),
    path('pokemonDetail/<int:pk>', views.PokemonDetail.as_view(), name='PokemonDetail'),
    
]