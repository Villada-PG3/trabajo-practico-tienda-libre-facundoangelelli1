from django.urls import path
from . import views

app_name = 'almacen'

urlpatterns = [
    # Usamos .as_view() para las nuevas vistas basadas en clases
    path('', views.HomeView.as_view(), name='home'),
    path('catalogo/', views.CatalogoView.as_view(), name='catalogo'),
    
    # Las basadas en funciones quedan igual
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca-de-mi'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
]