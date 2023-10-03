from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}  # Saca los mensajes de ayuda
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))
    password2 = forms.CharField(label='Repeat the Password', widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))
    pais = forms.CharField(max_length=30, label='Country', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))  

    last_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    first_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))

    class Meta:
        model = User
        fields = ['password1', 'password2', 'last_name', 'first_name', 'pais']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'