from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import PublicacionesForm
from .models import Publicacion

# Create your views here.

# Crear nuevas publicaciones
def nueva_publicacion_view(request):
    if request.method == 'POST':
        form = PublicacionesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "Blog/Publicaciones.html",
                {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )
    else:
        form = PublicacionesForm()
    return render(request,'Blog/NuevaPublicacion2.html',{'form':form})

#Ver todas las publicaciones
def Publicaciones(request):
    t_publicaciones = Publicacion.objects.all()
    template = loader.get_template('Blog/publicaciones.html')
    context = {'t_publicaciones':t_publicaciones}

    return HttpResponse(template.render(context,request))

#Ver solo las publicaciones del usuario registrado
def mis_publicaciones(request):
    tm_publicaciones = Publicacion.objects.filter(autor=request.user.id)
    return render(request, 'blog/MisPublicaciones.html', {'tm_publicaciones': tm_publicaciones})

#Acerca De
def VerAcercaDe(request):
    return render(request,'blog/About.html')

def VistaReiniciarLog(request):
    return render(request, 'blog/login.html') 


##############################
##          LOGIN           ##
##############################

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def VistaLogIn(request):

    if request.user.is_authenticated:
        return render(
            request,
            "Blog/Publicaciones.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "Blog/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "Blog/Publicaciones.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "Blog/login.html",
                {"form": formulario}
            )



from django.contrib.auth import logout
from django.shortcuts import render, redirect

def VistaLogOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Blog/login.html')  # Cambia 'nombre_de_la_vista_login' por el nombre real de tu vista de login
    return render(request, 'Blog/logout.html')  # Ajusta 'Blog/logout.html' según tu estructura de carpetas y archivos

# Otra opción, usando una función llamada logout_view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Blog/login.html')  # Cambia 'nombre_de_la_vista_login' por el nombre real de tu vista de login
    return render(request, 'Blog/logout.html')  # Ajusta 'Blog/logout.html' según tu estructura de carpetas y archivos

#########################
##      Registro       ##
#########################

from .forms import form_CrearUsuario, form_EditarUsuario
from django.contrib.auth.views import PasswordChangeView


def v_registro(request):

    if request.method == "GET":
        return render(
            request,
            "Blog/registro.html",
            {"form": form_CrearUsuario()}
        )
    else:
        formulario = form_CrearUsuario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = datos["username"]
            formulario.save()

            return render(
                request,
                "Blog/Publicaciones.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "Blog/registro.html",
                {"form": formulario}
            )

