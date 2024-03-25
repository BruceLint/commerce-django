from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto, Variation
from .models import Carrito, ArticuloCarrito
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from django.http import HttpResponse

def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito


def agregar_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id) #get the producto
    producto_variation = []
    if request.method == 'POST':
        for articulo in request.POST:
            key = articulo
            valor = request.POST[key]

            try:
                variation = Variation.objects.get(producto=producto, variation_categoria__iexact=key, variation_valor__iexact=valor)
                producto_variation.append(variation)
            except:
                pass


    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request)) #get the cart using the cart id
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            carrito_id = _carrito_id(request)
        )
    carrito.save()
    is_articulo_carrito_exists = ArticuloCarrito.objects.filter(producto=producto, carrito=carrito).exists()
    if is_articulo_carrito_exists:
        articulo_carrito = ArticuloCarrito.objects.filter(producto=producto, carrito=carrito)
        # existing_variations -> database
        # current_variation -> prodcuto variation
        # item_id
        ex_var_list = []
        id = []
        for articulo in articulo_carrito:
            existing_variation = articulo.variations.all()
            ex_var_list.append(list(existing_variation))
            id.append(articulo.id)

        print(ex_var_list)

        if producto_variation in ex_var_list:
            # increase cart item Quantity
            index = ex_var_list.index(producto_variation)
            articulo_id = id[index]
            articulo = ArticuloCarrito.objects.get(producto=producto, id=articulo_id)
            articulo.cantidad += 1
            articulo.save()

        else:
            articulo = ArticuloCarrito.objects.create(producto=producto, cantidad=1, carrito=carrito)
            if len(producto_variation) > 0:
                articulo.variations.clear()
                articulo.variations.add(*producto_variation)
            articulo.save()
    else:
        articulo_carrito = ArticuloCarrito.objects.create(
            producto = producto,
            cantidad = 1,
            carrito = carrito,
        )
        if len(producto_variation) > 0:
            articulo_carrito.variations.clear()
            articulo_carrito.variations.add(*producto_variation)
        articulo_carrito.save()
    return redirect('carrito')


def remover_carrito(request, producto_id, articulo_carrito_id):
    carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    producto = get_object_or_404(Producto, id=producto_id)
    try:
        articulo_carrito = ArticuloCarrito.objects.get(producto=producto, carrito=carrito, id=articulo_carrito_id)
        if articulo_carrito.cantidad > 1:
            articulo_carrito.cantidad -= 1
            articulo_carrito.save()
        else:
            articulo_carrito.delete()
    except:
        pass
    return redirect('carrito')

def remover_articulo_carrito(request, producto_id, articulo_carrito_id):
    carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    producto = get_object_or_404(Producto, id=producto_id)
    articulo_carrito = ArticuloCarrito.objects.get(producto=producto, carrito=carrito, id=articulo_carrito_id)
    articulo_carrito.delete()
    return redirect('carrito')

def carrito(request, total=0, cantidad=0, articulo_carrito=None):
    try:
        impuesto = 0
        total_final = 0
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
        articulos_carrito = ArticuloCarrito.objects.filter(carrito=carrito, esta_activo=True)
        for articulo_carrito in articulos_carrito:
            total += (articulo_carrito.producto.precio * articulo_carrito.cantidad)
            cantidad += articulo_carrito.cantidad
        impuesto = (2 * total)/100
        total_final = total + impuesto
    except ObjectDoesNotExist:
        pass #just ignoe

    context = {
        'total': total,
        'cantidad': cantidad,
        'articulos_carrito': articulos_carrito,
        'impuesto': impuesto,
        'total_final': total_final,
    }
    return render(request, 'tienda/carrito.html', context)
