from django.contrib import admin
from django.utils.html import format_html
from almacen.models import Producto, Categoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'mostrar_miniatura')

    readonly_fields = ('mostrar_imagen_detalle',)

    def mostrar_miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.imagen.url)
        return "Sin imagen"
    
    mostrar_miniatura.short_description = 'Miniatura'

    def mostrar_imagen_detalle(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 300px; border: 1px solid #ccc;" />', obj.imagen.url)
        return "Sin imagen"

    mostrar_imagen_detalle.short_description = 'Previsualización de la Imagen'


admin.site.register(Categoria)
# Register your models here.