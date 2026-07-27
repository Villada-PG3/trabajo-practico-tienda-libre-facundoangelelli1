from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre= models.CharField()
    cantidad= models.IntegerField()
