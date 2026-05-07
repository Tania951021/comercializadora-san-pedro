from django.urls import path
from . import views

urlpatterns = [

    # PAGINA PRINCIPAL
    path(
        '',
        views.inicio,
        name='inicio'
    ),

    # CRUD PRODUCTOS
    path(
        'productos/',
        views.lista_productos,
        name='lista_productos'
    ),

    path(
        'crear/',
        views.crear_producto,
        name='crear_producto'
    ),

    path(
        'editar/<int:id>/',
        views.editar_producto,
        name='editar_producto'
    ),

    path(
        'eliminar/<int:id>/',
        views.eliminar_producto,
        name='eliminar_producto'
    ),

    # FORMULARIO CONTACTO
    path(
        'contacto/',
        views.contacto,
        name='contacto'
    ),

]