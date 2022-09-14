from django.shortcuts import render
from . import views

# Create your views here.
from django.http import HttpResponse

class Pokemon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, weight, level):
    self.name = name
    self.type = type
    self.weight = weight
    self.level = level

pokemons = [
  Pokemon('Squirtle', 'Water', '10', 15),
  Pokemon('Pikachi', 'Electric', '15', 67),
  Pokemon('Charmander', 'Fire', '7', 12)
]

#Define the home view 
def home(request):
    return HttpResponse('<h1> GOTTA CATCH EM ALL <h1>')
def about(request):
    return render(request, 'about.html')
def pokedex(request):
  return render(request, 'pokemon/index.html', { 'pokemons': pokemons})
