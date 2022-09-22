from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import Pokemon
from .forms import LocationForm
from django.shortcuts import render, redirect

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
  location_form = LocationForm()
  return render(request, 'pokemon/detail.html', {'pokemon': pokemon, 'location_form': location_form})
def add_feeding(request, cat_id):
  form = LocationForm(request.POST)
  if form.is_valid():
    new_location = form.save(commit=False)
    new_location.pokemon_id = pokemon_id
    new_location.save()
  return redirect('detail', pokemon_id=pokemon_id)
