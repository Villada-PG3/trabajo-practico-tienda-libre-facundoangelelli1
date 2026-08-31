from django.shortcuts import render
from .models import Producto

def home(request):
    contexto = {
        "titulo": "Ofertas de la semana",
        "usuario_logueado": True,
        "productos_destacados": [
            {"nombre": "Auriculares Bluetooth", "precio": 15999, "stock": 32},
            {"nombre": "Mouse inalámbrico", "precio": 8499, "stock": 18},
            {"nombre": "Teclado mecánico", "precio": 24999, "stock": 7},
            {"nombre": "Webcam HD", "precio": 12999, "stock": 4},
            {"nombre": "Pendrive 64GB", "precio": 5999, "stock": 1},
            {"nombre": "Hub USB-C", "precio": 7299, "stock": 0},
        ],
    }
    return render(request, "almacen/home.html", contexto)


def acerca_de_mi(request):
    return render(request, "almacen/acerca-de-mi.html")

def productos(request):
    productos_db = Producto.objects.all()  # Variable en minúscula
    
    contexto = {
        "productos": productos_db
    }
    return render(request, "almacen/productos.html", contexto)