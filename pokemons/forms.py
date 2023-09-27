from django import forms
from .models import *

class PokemonForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    attack = forms.IntegerField()
    defense = forms.IntegerField()
    health = forms.IntegerField()
    image = forms.ImageField()
    