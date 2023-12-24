from django import forms
from .models import Publicacion

class PublicacionesForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['autor','titulo','subtitulo','comentarios','imagen']


######################
##      REGISTRO    ##
######################
        
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel


class form_CrearUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}


class form_EditarUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


