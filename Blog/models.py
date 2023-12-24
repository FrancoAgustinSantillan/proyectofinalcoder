from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


# Create your models here.

class Publicacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100,default = '')
    subtitulo = models.CharField(max_length=100,default = '')
    comentarios = models.CharField(max_length=3000,default = '')
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comentarios}"
