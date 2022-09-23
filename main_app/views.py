from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LocationForm
from django.shortcuts import render, redirect
from .models import Items, Pokemon, Location
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse

class CreatePokemon(CreateView):
  model = Pokemon
  fields = '__all__'
  success_url = '/pokemon/'
  @login_required
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

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
@login_required
def pokedex(request):
  pokemon = Pokemon.objects.filter(user=request.user)
  return render(request, 'pokemon/index.html', { 'pokemon': pokemon})
@login_required
def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id = pokemon_id)
  items_pokemon_doesnt_have = Items.objects.exclude(id__in = pokemon.items.all().values_list('id'))
  location_form = LocationForm()
  return render(request, 'pokemon/detail.html', {'pokemon': pokemon, 'location_form': location_form, 'items': items_pokemon_doesnt_have})
@login_required
def add_location(request, pokemon_id):
  form = LocationForm(request.POST)
  if form.is_valid():
    new_location = form.save(commit=False)
    new_location.pokemon_id = pokemon_id
    new_location.save()
  return redirect('detail', pokemon_id=pokemon_id)
@login_required
def assoc_items(request, pokemon_id, items_id):
  Pokemon.objects.get(id=pokemon_id).items.add(items_id)
  return redirect('detail', pokemon_id=items_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)