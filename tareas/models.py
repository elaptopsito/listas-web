from django.db import models
from django.conf import settings

# Create your models here.
class Tarea(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tareas",    
    )
    texto = models.CharField(max_length=200)
    hecha = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
        