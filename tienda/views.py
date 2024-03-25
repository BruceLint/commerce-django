from django.shortcuts import render, get_object_or_404
from .models import Producto
from categoria.models import Categoria
from carrito.models import ArticuloCarrito
from django.db.models import Q

from carrito.views import _carrito_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
# Create your views here.

def tienda(request, categoria_slug=None):
    categorias = None
    productos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        productos = Producto.objects.filter(categoria=categorias, esta_disponible=True)
        paginator = Paginator(productos, 1)
        page = request.GET.get('page')
        paged_productos = paginator.get_page(page)
        producto_count = productos.count()
    else:
        productos = Producto.objects.all().filter(esta_disponible=True).order_by('id')
        paginator = Paginator(productos, 6)
        page = request.GET.get('page')
        paged_productos = paginator.get_page(page)
        producto_count = productos.count()

    context = {
        'productos': paged_productos,
        'producto_count': producto_count,
    }
    return render(request, 'tienda/tienda.html', context)


def detalle_producto(request, categoria_slug, producto_slug):
    try:
        producto_unico = Producto.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
        en_carrito = ArticuloCarrito.objects.filter(carrito__carrito_id=_carrito_id(request), producto=producto_unico).exists()
    except Exception as e:
        raise e

    context = {
        'producto_unico': producto_unico,
        'en_carrito': en_carrito,
    }
    return render(request, 'tienda/detalle_producto.html', context)


def busqueda(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            productos = Producto.objects.order_by('-fecha_creada').filter(Q(descripcion__icontains=keyword) | Q(nombre_producto__icontains=keyword))
            producto_count = productos.count()
    context = {
        'productos': productos,
        'producto_count': producto_count, 
    }
    return render(request, 'tienda/tienda.html', context)
