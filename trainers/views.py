from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trainer
# Class Based Views imports
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView



# Class Based Views
class TrainerList(ListView):
    model = Trainer
    
class TrainerDetail(DetailView):
    model = Trainer
        
class TrainerCreate(LoginRequiredMixin, CreateView):
    model = Trainer
    form_class = (
        TrainerForm
    )
    success_url = '/trainers/trainerList'
    
class TrainerUpdate(LoginRequiredMixin, UpdateView):
    model = Trainer
    form_class = (
        TrainerForm
    )
    success_url = '/trainers/trainerList'
    
class TrainerDelete(LoginRequiredMixin, DeleteView):
    model = Trainer
    success_url = '/trainers/trainerList'