from django import forms
from .models import *
from trainers.models import Trainer

class GymForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    master = forms.ModelChoiceField(
        queryset= Trainer.objects.all(),
        widget= forms.RadioSelect
    )