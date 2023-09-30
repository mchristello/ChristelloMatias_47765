from django import forms
from .models import *

class PokemonForm(forms.ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form_input'}))
    type = forms.CharField(label='type', widget=forms.TextInput(attrs={'class': 'form_input'}))
    attack = forms.IntegerField(label='attack', widget=forms.NumberInput(attrs={'class': 'form_input'}))
    defense = forms.IntegerField(label='defense', widget=forms.NumberInput(attrs={'class': 'form_input'}))
    health = forms.IntegerField(label='health', widget=forms.NumberInput(attrs={'class': 'form_input'}))
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Pokemon
        fields = ['name', 'type', 'attack', 'defense', 'health', 'image']