from django import forms
from pokemons.models import Pokemon
from .models import Trainer


class TrainerForm(forms.ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form_input'}))
    lastname = forms.CharField(label='lastname', widget=forms.TextInput(attrs={'class': 'form_input'}))
    favorite_type = forms.CharField(label='favorite_type', widget=forms.TextInput(attrs={'class': 'form_input'}))
    owned_pokemons = forms.ModelMultipleChoiceField(
        queryset= Pokemon.objects.all(),
        widget= forms.CheckboxSelectMultiple,
    )
    
    class Meta:
        model = Trainer
        fields = ['name', 'lastname', 'favorite_type', 'owned_pokemons']