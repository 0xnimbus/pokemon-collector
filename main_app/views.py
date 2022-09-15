from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import Pokemon

# Create your views here.
from django.http import HttpResponse

class CreatePokemon(CreateView):
  model = Pokemon
  fields = '__all__'
  success_url = '/pokemon/'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['name', 'type', 'weight']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon'

#Define the home view 
def home(request):
    return HttpResponse('<h1> GOTTA CATCH EM ALL <h1>')
def about(request):
    return render(request, 'about.html')
def pokedex(request):
  return render(request, 'pokemon/index.html', { 'pokemons': pokemons})
def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id = pokemon_id)
  return render(request, 'pokemon/detail.html', {'pokemon': pokemon})
