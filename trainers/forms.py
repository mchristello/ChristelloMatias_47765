from django import forms
from pokemons.models import Pokemon

class TrainerForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    favorite_type = forms.CharField()
    owned_pokemons = forms.ModelMultipleChoiceField(
        queryset= Pokemon.objects.all(),
        widget= forms.CheckboxSelectMultiple()
    )
    