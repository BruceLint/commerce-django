from django.db import models
from tienda.models import Producto, Variation

# Create your models here.

class Carrito(models.Model):
    carrito_id = models.CharField(max_length=250, blank=True)
    fecha_agregado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carrito_id


class ArticuloCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    esta_activo = models.BooleanField(default=True)

    def sub_total(self):
        return self.producto.precio * self.cantidad

    def __unicode__(self):
        return self.producto
