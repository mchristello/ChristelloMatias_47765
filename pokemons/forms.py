from django import forms
from .models import *

class PokemonForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    type = forms.CharField(label='Type', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    attack = forms.IntegerField(label='Attack', widget=forms.NumberInput(attrs={'class': 'form_input m-2'}))
    defense = forms.IntegerField(label='Defense', widget=forms.NumberInput(attrs={'class': 'form_input m-2'}))
    health = forms.IntegerField(label='Health', widget=forms.NumberInput(attrs={'class': 'form_input m-2'}))
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Pokemon
        fields = ['name', 'type', 'attack', 'defense', 'health', 'image']
        widget = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }