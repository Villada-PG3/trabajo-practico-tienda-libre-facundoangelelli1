from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'almacen/home.html'

class AcercaDeMiView(TemplateView):
    template_name = 'almacen/acerca-de-mi.html'

# Aquí sigues manteniendo tu ProductoTemplateViews