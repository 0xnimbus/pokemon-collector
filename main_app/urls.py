from django.urls import path
from . import views

# Add the Cat class & list and view function below the imports


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokedex, name='pokedex'),
    path('pokemon/<int:pokemon_id>/', views.cats_detail, name = 'detail'),
    path('pokemon/create/'. views.PokemonCreate.as_view(), name='pokemon_create')
    path('pokemon/<int:pk>/update/', views.CatUpdate.as_view(), name='pokemon_update'),
    path('pokemon/<int:pk>/delete/', views.CatDelete.as_view(), name='pokemon_delete'),
     path('pokemon/<int:pk_id>/add_location/', views.add_location, name='add_location'),
]