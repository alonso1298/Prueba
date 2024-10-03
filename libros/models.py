from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del autor
    fecha_nacimiento = models.DateField()      # Fecha de nacimiento del autor

    def __str__(self):
        return self.nombre  # Representación en cadena del autor

class Libro(models.Model):
    titulo = models.CharField(max_length=200)   # Título del libro
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Relación con el modelo Autor
    fecha_publicacion = models.DateField()      # Fecha de publicación del libro

    def __str__(self):
        return self.titulo  # Representación en cadena del libro


