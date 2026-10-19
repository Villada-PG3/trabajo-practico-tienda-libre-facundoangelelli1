from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Producto

# 1. Reescribir Home como TemplateView
class HomeView(TemplateView):
    template_name = 'almacen/home.html'

    # Sobrescribimos este método para enviar datos adicionales al template (Práctica 5)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traemos los 3 productos más recientes
        context['productos_recientes'] = Producto.objects.order_by('-fecha_creacion')[:3]
        return context

# 2. Reescribir Catálogo como ListView
class CatalogoView(ListView):
    model = Producto
    template_name = 'almacen/catalogo.html'
    context_object_name = 'productos' # Así iteramos con {% for producto in productos %}

# Mantenemos las que todavía no cambiamos (Acerca de mi y Detalle)
def acerca_de_mi(request):
    return render(request, 'almacen/acerca-de-mi.html')

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'almacen/detalle.html', {'producto': producto})