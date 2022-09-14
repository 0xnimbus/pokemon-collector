from django.urls import path
from . import views

# Add the Cat class & list and view function below the imports


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
     path('pokemon/', views.pokedex, name='pokedex'),
]