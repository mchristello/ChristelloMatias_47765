from django import forms
from pokemons.models import Pokemon
from .models import Trainer


class TrainerForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    favorite_type = forms.CharField(label='Favorite Type', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    owned_pokemons = forms.ModelMultipleChoiceField(
        queryset= Pokemon.objects.all(),
        widget= forms.CheckboxSelectMultiple,
        label='Owned Pokemons',
        required=False
    )
    
    class Meta:
        model = Trainer
        fields = ['name', 'lastname', 'favorite_type', 'owned_pokemons']