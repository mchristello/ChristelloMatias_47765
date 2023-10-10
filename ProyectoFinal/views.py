from django.shortcuts import render, HttpResponse
from pokemons.models import Pokemon
from trainers.models import Trainer
from gyms.models import Gym

# Vistas generales
def home_page(request):
    
    user = request.user
    if user:
        return render(request, 'home.html', { 'user': user })
    
    return render(request, 'home.html')

# Vista de Busquedas
def page_search(request):
    
    query = request.GET.get('query', '')
    element_type = request.GET.get('element_type', '')
    print(element_type)
    
    if query and element_type:
        
        if element_type == 'pokemon':
            result = Pokemon.objects.filter(name__icontains=query)
            print(result)
        if element_type == 'trainer':
            result = Trainer.objects.filter(name__icontains=query)
            print(result)
        if element_type == 'gym':
            result = Gym.objects.filter(name__icontains=query)
            print(result)
        return render(request, 'search_result.html', { 'query': query, 'result': result, 'element_type': element_type})
    
    else:
        
        advice = f'No se enviaron datos!'
        
    return HttpResponse(advice)

def about_me(request):
    
    return render(request, 'about_me.html')