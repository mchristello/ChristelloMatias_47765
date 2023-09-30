from django import forms
from .models import *
from trainers.models import Trainer
from .models import Gym

class GymForm(forms.ModelForm):
    name = forms.CharField()
    type = forms.CharField()
    master = forms.ModelChoiceField(
        queryset= Trainer.objects.all(),
        widget= forms.RadioSelect
    )
    class Meta:
        model = Gym
        fields = ['name', 'type', 'master']