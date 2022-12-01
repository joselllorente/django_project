from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    #email = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellidos} {self.dni} {self.email}"


class Coche(models.Model):
    matricula = models.CharField(max_length=40)
    marca = models.CharField(max_length=60)
    combustible = models.CharField(max_length=9)
    color = models.CharField(max_length=100, null=True)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Coche: {self.id} {self.matricula} {self.marca} {self.combustible} {self.color} Cliente: {self.cliente.nombre if self.cliente!= None else ''}"