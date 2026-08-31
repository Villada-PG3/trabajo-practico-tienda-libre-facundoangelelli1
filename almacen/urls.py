from django.urls import path
from . import views

app_name = 'almacen'

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca-de-mi'),
]
