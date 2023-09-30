from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import Trainer
# Class Based Views imports
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView


# Create your views here.
def views_trainer(request):
    all_trainers = Trainer.objects.all()
    if request.method == 'POST':
        
        trainerform = TrainerForm(request.POST)
        if trainerform.is_valid():
            info = trainerform.cleaned_data
            trainer = Trainer(name=info['name'], lastname=info['lastname'], favorite_type=info['favorite_type'])
            trainer.save()
            return render(request, 'trainers/trainer.html', {'all_trainers': all_trainers, 'trainerform': trainerform})
    else:
        trainerform = TrainerForm()
    return render(request, 'trainers/master.html', {'all_trainers': all_trainers, 'trainerform': trainerform})

# Class Based Views
class TrainerList(ListView):
    model = Trainer
    
class TrainerDetail(DetailView):
    model = Trainer
        
class TrainerCreate(CreateView):
    model = Trainer
    form_class = (
        TrainerForm
    )
    success_url = '/trainers/trainerList'
    
class TrainerUpdate(UpdateView):
    model = Trainer
    form_class = (
        TrainerForm
    )
    success_url = '/trainers/trainerList'
    
class TrainerDelete(DeleteView):
    model = Trainer
    success_url = '/trainers/trainerList'