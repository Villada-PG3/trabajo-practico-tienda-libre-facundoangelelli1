from django.db import models


class Categoria(models.Model):
    nombre = models.CharField( max_length=50, unique=True)
    slug= models.SlugField(unique=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    def __str__(self):
        return self.nombre
# Create your models here.
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, related_name= "productos", null= True, blank=True )
    nombre= models.CharField(max_length= 10)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad= models.IntegerField()
    marca = models.CharField(max_length= 5, default="sin marca")

    def __str__(self):
            return self.nombre
