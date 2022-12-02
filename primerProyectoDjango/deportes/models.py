from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    equipo = models.CharField(max_length=20)
    edad = models.IntegerField(max_length=2)
    nacionalidad = models.CharField(max_length=30)
    posicion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.id}:{self.nombre}:{self.edad}:{self.nacionalidad}:{self.equipo}:{self.posicion}"