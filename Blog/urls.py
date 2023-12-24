from django.contrib import admin
from django.urls import path, include
from .views import nueva_publicacion_view,Publicaciones,VistaLogIn,VistaLogOut,mis_publicaciones,VerAcercaDe,v_registro
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Blog'

urlpatterns = [
 path('Publicaciones/',views.Publicaciones,name='blog'),
 path('NuevaPublicacion/',views.nueva_publicacion_view,name='NuevaPubli'),
 path('MisPublicaciones/',views.mis_publicaciones,name='MiBlog'),
 path('About/',views.VerAcercaDe,name='About'),
 path("registro/", views.v_registro, name="registro"),
 path("login/", views.VistaLogIn, name="login"),
 path('logout/', auth_views.LogoutView.as_view(next_page='VistaReiniciarLog'), name='logout'),
]
    