from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    contexto = {
        "titulo": "Ofertas de la semana",
        "usuario_logueado": True ,
        "productos_destacados": [
            {"nombre": "Auriculares Bluetooth", "precio": 15999, "stock": 32},
            {"nombre": "Mouse inalámbrico", "precio": 8499, "stock": 18},
            {"nombre": "Teclado mecánico", "precio": 24999, "stock": 7},
            {"nombre": "Webcam HD", "precio": 12999, "stock": 4},
            {"nombre": "Pendrive 64GB", "precio": 5999, "stock": 2},
            {"nombre": "Hub USB-C", "precio": 7299, "stock": 0},
            {"nombre": "Celular", "precio": None, "stock": 2},
        ],
    }
    return render(request, "almacen/home.html", contexto)


def acerca_de_mi(request):
    return render(request, "almacen/acerca-de-mi.html")


def catalogo(request):
    producto = Producto.objects.filter(activo = True).order_by("-fecha_creacion")[:3]
    context = {"productos": producto}
    return render(request, "almacen/catalogo.html", context)

def detalle_producto(request, pk):
    # Intentamos obtener el producto, si no existe, devuelve un error 404
    producto = get_object_or_404(Producto, pk=pk)
    
    # Pasamos el producto al template
    return render(request, 'almacen/detalle.html', {'producto': producto})