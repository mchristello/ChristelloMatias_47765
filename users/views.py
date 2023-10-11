from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from .forms import *
# Decorators Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Vista de Login 
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST) # Recibe la info del formulario
        if login_form.is_valid():
            login_info = login_form.cleaned_data
            username = login_info.get('username')
            password = login_info.get('password')            
            
            user = authenticate(username=username, password=password) # validación del login
            if user:
                login(request, user) # Se inicia sesión si las credentials son correctas
                return render(request, 'home.html', { 'user': user })
            else: 
                return render(request, 'users/login.html', { 'message': f'Error authenticating...'})
    login_form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': login_form })

def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            register_form.save()
            return render(request, 'home.html', { 'message': f'User {username} registration successful.'})
        
    else: 
        register_form = UserRegisterForm()
        
    return render(request, 'users/register.html', { 'form': register_form })

# Vista de editar el perfil
@login_required
def editProfile(request):

    user = request.user
    if request.method == 'POST':

        user_form = UserEditForm(request.POST, instance=request.user)

        if user_form.is_valid():

            form_info = user_form.cleaned_data
            
            user.email = form_info['email']
            user.last_name = form_info['last_name']
            user.first_name = form_info['first_name']

            user.save()

            return render(request, "home.html")

    else:

        user_form = UserEditForm(initial={'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}, instance=request.user)

    return render(request, "users/edit_profile.html", {"user_form": user_form, "user": user})

@login_required
def addAvatar(request):
    user = request.user

    if request.method == 'POST':
        avatar_form = AvatarFormulario(request.POST, request.FILES, initial={'user': user})
        if avatar_form.is_valid():
            
            avatar = avatar_form.save(commit=False)
            avatar.user = user
            avatar.save()
            
            return render(request, "home.html")  
        
    else:
        user = request.user
        avatar_form = AvatarFormulario(initial={'user': user})
    
    return render(request, "users/add_avatar.html", {"avatar_form": avatar_form, 'User': user})

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html' 
    success_url = '/users/login'