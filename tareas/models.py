from django.db import models

# Create your models here.
class Tarea(models.Model):
    texto = models.CharField(max_length=200)
    hecha = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
        