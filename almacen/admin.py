from django.contrib import admin
from .models import Producto
admin.site.register(Producto)
from .models import Categoria
admin.site.register(Categoria)
# Register your models here.
