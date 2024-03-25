from django.contrib import admin
from .models import Producto, Variation
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio', 'disponibilidad', 'categoria', 'fecha_modificada', 'esta_disponible')
    prepopulated_fields = {'slug': ('nombre_producto',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('producto', 'variation_categoria', 'variation_valor', 'esta_activo')
    list_editable = ('esta_activo'),
    list_filter = ('producto', 'variation_categoria', 'variation_valor')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Variation, VariationAdmin)
