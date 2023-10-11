from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}  # Saca los mensajes de ayuda
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form_input m-2 disable'}))
    country = forms.CharField(max_length=30, label='Country', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))  

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form_input m-2'}))
    password1 = forms.CharField(label='Password to Confirm', widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))
    password2 = forms.CharField(label='Repeat the Password', widget=forms.PasswordInput(attrs={'class': 'form_input m-2'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'country', 'password1', 'password2']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(AvatarFormulario, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['user'].disabled = True