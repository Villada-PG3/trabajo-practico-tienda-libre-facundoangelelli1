from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ProductoTemplateViews(TemplateView):
    template_name= "productos.html"