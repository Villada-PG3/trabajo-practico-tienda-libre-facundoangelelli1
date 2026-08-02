from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True) # "Hogar y Jaridin"
    slug = models.SlugField(max_length=100, unique=True) # "hogar-y-jardin"

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos',
        null = True,
        blank = True # temporal hasta que se agregue la categoria a todos los productos
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    marca = models.CharField(max_length=50, default='Marca Desconocida')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} - {self.marca} - ${self.precio} - Stock: {self.stock}'