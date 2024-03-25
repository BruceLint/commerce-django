from django.contrib import admin
from .models import Carrito, ArticuloCarrito
# Register your models here.

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito_id','fecha_agregado')

class CarritoArticuloAdmin(admin.ModelAdmin):
    list_display = ('producto','carrito', 'cantidad', 'esta_activo')

admin.site.register(Carrito, CarritoAdmin)
admin.site.register(ArticuloCarrito, CarritoArticuloAdmin)
