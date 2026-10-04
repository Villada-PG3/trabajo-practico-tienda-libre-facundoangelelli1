from django.shortcuts import render, get_object_or_404
from .models import Producto




def acerca_de_mi(request):
    return render(request, "almacen/acerca-de-mi.html")


def catalogo(request):
    producto = Producto.objects.filter(activo = True).order_by("-fecha_creacion")
    context = {"productos": producto}
    return render(request, "almacen/catalogo.html", context)
def home(request):
    producto = Producto.objects.filter(activo = True).order_by("-fecha_creacion")[:3]
    context = {"productos": producto}
    return render(request, "almacen/home.html", context)
def detalle_producto(request, pk):
    # Intentamos obtener el producto, si no existe, devuelve un error 404
    producto = get_object_or_404(Producto, pk=pk)
    
    # Pasamos el producto al template
    return render(request, 'almacen/detalle.html', {'producto': producto})