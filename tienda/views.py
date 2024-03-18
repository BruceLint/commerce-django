from django.shortcuts import render, get_object_or_404
from .models import Producto
from categoria.models import Categoria

# Create your views here.

def tienda(request, categoria_slug=None):
    categorias = None
    productos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        productos = Producto.objects.filter(categoria=categorias, esta_disponible=True)
        producto_count = productos.count()
    else:
        productos = Producto.objects.all().filter(esta_disponible=True)
        producto_count = productos.count()

    context = {
        'productos': productos,
        'producto_count': producto_count,
    }
    return render(request, 'tienda/tienda.html', context)


def detalle_producto(request, categoria_slug, producto_slug):
    try:
        producto_unico = Producto.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
    except Exception as e:
        raise e

    context = {
        'producto_unico': producto_unico,
    }
    return render(request, 'tienda/detalle_producto.html', context)
