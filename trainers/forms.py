from django import forms
from pokemons.models import Pokemon
from .models import Trainer


class TrainerForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    favorite_type = forms.CharField(label='Favorite Type', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    owned_pokemons = forms.ModelMultipleChoiceField(
        queryset= Pokemon.objects.filter(trainer=None),
        widget= forms.CheckboxSelectMultiple,
        label='Owned Pokemons',
        required=False
    )
    
    class Meta:
        model = Trainer
        fields = ['name', 'lastname', 'favorite_type', 'owned_pokemons']
    
    # Funcionalidad para modificar el campo "trainer" del model Pokemon según los agregue un nuevo Trainer a su stack.
    def save(self, commit=True):
        trainer = super(TrainerForm, self).save(commit=commit)
        
        if commit:
            # Obtén los Pokémon seleccionados y actualiza su trainer
            selected_pokemons = self.cleaned_data.get('owned_pokemons')
            if selected_pokemons:
                for pokemon in selected_pokemons:
                    pokemon.trainer = trainer
                    pokemon.save()

        return trainer