from django.shortcuts import render
from . import Pokemon

# Create your views here.
from django.http import HttpResponse


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
