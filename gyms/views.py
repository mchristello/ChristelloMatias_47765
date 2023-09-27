from django.shortcuts import render
from .models import Gym
from .forms import *
# Class based imports
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

# Create your views here.
def views_gyms(request):
    all_gyms = Gym.objects.all()
    if request.method == 'POST':
        gymform = GymForm(request.POST)
        if gymform.is_valid():
            info = gymform.cleaned_data
            gym = Gym(name=info['name'], type=info['type'], master=info['master'])
            gym.save()
            return render(request, 'gyms/gym_list.html', {'all_gyms': all_gyms, 'gymform': gymform })
    else:
        gymform = GymForm()
    return render(request, 'gyms/gym_list.html', {'all_gyms': all_gyms, 'gymform': gymform })

# Class based Views
class GymList(ListView):
    model = Gym

class GymDetail(DetailView):
    model = Gym
    
class GymCreate(CreateView):
    model = Gym
    fields = ['name', 'type', 'master']
    success_url = '/gymsList'
    
class GymUpdate(UpdateView):
    model = Gym
    fields = ['name', 'type', 'master']
    success_url = '/gymsList'
    
class GymDelete(DeleteView):
    model = Gym
    success_url = '/gymsList'