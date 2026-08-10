from django.urls import path
from .views import HomeView, AcercaDeMiView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('acerca-de-mi/', AcercaDeMiView.as_view(), name='acerca_de_mi'),
]