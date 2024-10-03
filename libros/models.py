from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del autor
    fecha_nacimiento = models.DateField()      # Fecha de nacimiento del autor

    def __str__(self):
        return self.nombre  # Representación en cadena del autor




