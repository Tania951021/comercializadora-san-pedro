from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Producto
from .forms import ProductoForm
from django.conf import settings
from django.http import JsonResponse
import logging
import requests
from django.urls import reverse

logger = logging.getLogger(__name__)


def inicio(request):
    lista_productos = Producto.objects.all()
    paginator = Paginator(lista_productos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'inventario/index.html',
        {
            'page_obj': page_obj
        }
    )

# READ
def lista_productos(request):
    lista_productos = Producto.objects.all()
    paginator = Paginator(lista_productos, 10)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    return render(
        request,
        'inventario/lista_productos.html',
        {'productos': productos}
)


# CREATE
def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('inicio') + '#servicios')

    return render(
        request,
        'inventario/crear_producto.html',
        {'form': form}
    )

# UPDATE
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(
        request.POST or None,
        instance=producto
    )
    if form.is_valid():
        form.save()
        return redirect(reverse('inicio') + '#servicios')

    return render(
        request,
        'inventario/editar_producto.html',
        {'form': form}
    )


# DELETE
def eliminar_producto(request, id):
    producto = get_object_or_404(
        Producto,
        id=id
    )
    if request.method == 'POST':
        producto.delete()
        return redirect(reverse('inicio') + '#servicios')

    return render(
        request,
        'inventario/eliminar_producto.html',
        {'producto': producto}
    )
    
def enviar_correo_brevo(nombre, correo, mensaje):
    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json"
    }

    data = {
        "sender": {
            "name": "Formulario Web",
            "email": settings.DEFAULT_FROM_EMAIL
        },
        "to": [
            {
                "email": settings.DEFAULT_FROM_EMAIL,
                "name": "Tania"
            }
        ],
        "subject": f"Nuevo mensaje de: {nombre}",
        "htmlContent": f"""
            <h3>Nuevo mensaje de contacto</h3>
            <p><b>Nombre:</b> {nombre}</p>
            <p><b>Correo:</b> {correo}</p>
            <p><b>Mensaje:</b><br>{mensaje}</p>
        """
    }

    # llamada HTTP rápida (sin SMTP, sin timeout)
    requests.post(url, json=data, headers=headers, timeout=10)


def contacto(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre', '').strip()
            correo = request.POST.get('correo', '').strip()
            mensaje = request.POST.get('mensaje', '').strip()

            if not nombre or not correo or not mensaje:
                return JsonResponse({'mensaje': '❌ Completa todos los campos'}, status=400)

            # Guarda en la base de datos
            contacto.objects.create(
                nombre=nombre,
                correo=correo,
                mensaje=mensaje
            )

            # Envía el correo por Brevo API
            enviar_correo_brevo(nombre, correo, mensaje)

            return JsonResponse({'mensaje': 'Mensaje enviado correctamente'})

        except Exception as e:
            error_texto = f"Error: {type(e).__name__} - {str(e)}"
            logger.error(error_texto)
            return JsonResponse({'mensaje': error_texto}, status=500)

    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



    
