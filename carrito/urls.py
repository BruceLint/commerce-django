from django.urls import path
from .import views

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('agregar_carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('remover_carrito/<int:producto_id>/<int:articulo_carrito_id>/', views.remover_carrito, name='remover_carrito'),
    path('remover_articulo_carrito/<int:producto_id>/<int:articulo_carrito_id>/', views.remover_articulo_carrito, name='remover_articulo_carrito'),
]
