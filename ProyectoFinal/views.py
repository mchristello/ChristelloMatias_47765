from django.shortcuts import render

def home_page(request):
    user = 'Matias'
    if user:
        return render(request, 'home.html', { 'user': user })
    return render(request, 'home.html')