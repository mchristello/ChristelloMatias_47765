from django import forms
from .models import *
from trainers.models import Trainer
from .models import Gym

class GymForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    type = forms.CharField(label='Type', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    master = forms.ModelChoiceField(
        queryset= Trainer.objects.all(),
        widget= forms.RadioSelect,
        required=False
    )
    class Meta:
        model = Gym
        fields = ['name', 'type', 'master']