from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proyecto(models.Model):
    proyecto_name = models.CharField(
        max_length=100, verbose_name="Nombre del Proyecto"
    )
    descripcion = models.TextField(verbose_name="Descripción")
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario"
    )
    def __str__(self):
        return self.proyecto_name
    
class Tarea(models.Model):
    task_name = models.CharField(
        max_length=100, verbose_name="Nombre de la Tarea"
    )
    completada = models.BooleanField(
        default=False, verbose_name="¿Completada?"
    )
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE
    )