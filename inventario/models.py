from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(max_length=100)

    descripcion = models.CharField(max_length=200)

    fecha_creacion = models.DateField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=100)

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fecha_ingreso = models.DateField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre