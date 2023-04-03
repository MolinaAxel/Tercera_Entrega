from django.db import models

class Materias(models.Model):
    Materia = models.TextField(max_length=30)
    descripcion = models.TextField(max_length=100)
    estado = models.TextField(max_length=20, default="por hacer")


    def terminar(self):
        self.estado = "terminado"

    def __str__(self):
        return f"{self.id} - {self.Materia} --- {self.descripcion} ({self.estado})"

class Personas(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)

    def __str__(self):
        return f"{self.id}-- {self.nombre} {self.apellido}"
    
class Compras(models.Model):
    producto = models.TextField(max_length=15, default="nada")
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.producto} --- {self.cantidad}"
