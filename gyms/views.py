from .models import Gym
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Class based imports
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView


# Class based Views
class GymList(ListView):
    model = Gym

class GymDetail(DetailView):
    model = Gym
    
class GymCreate(LoginRequiredMixin, CreateView):
    model = Gym
    form_class = (
        GymForm
    )
    success_url = '/gyms/gymList'
    
class GymUpdate(LoginRequiredMixin, UpdateView):
    model = Gym
    form_class = (
        GymForm
    )
    success_url = '/gyms/gymList'
    
class GymDelete(LoginRequiredMixin, DeleteView):
    model = Gym
    success_url = '/gyms/gymList'