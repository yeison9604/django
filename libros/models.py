from django.db import models


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=20)
    autor = models.CharField(max_length=50)
    estado = models.BooleanField(default=0)
    stock = models.IntegerField(default=0)
    fecha_registro = models.DateField(auto_now_add=True, null=True, blank=True)

