from .models import Carrito, ArticuloCarrito
from .views import _carrito_id


def contador(request):
    carrito_conteo = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            carrito = Carrito.objects.filter(carrito_id=_carrito_id(request))
            articulos_carrito = ArticuloCarrito.objects.all().filter(carrito=carrito[:1])
            for articulo_carrito in articulos_carrito:
                carrito_conteo += articulo_carrito.cantidad
        except Carrito.DoesNotExist:
            carrito_conteo = 0
    return dict(carrito_conteo=carrito_conteo)
