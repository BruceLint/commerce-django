from django.db import models
from categoria.models import Categoria
from django.urls import reverse
# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='fotos/productos')
    disponibilidad = models.IntegerField()
    esta_disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('detalle_producto', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return self.nombre_producto
