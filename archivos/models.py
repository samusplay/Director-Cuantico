from django.db import models

# Create your models here.
class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    ruta = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre