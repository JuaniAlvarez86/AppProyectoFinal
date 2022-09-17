from django.db import models

# Create your models here.
class Marca(models.Model):

    nombre=models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)

    def __str__(self):
     return f" nombre: {self.nombre} --- nacionalidad: {self.nacionalidad}"


class Modelo(models.Model):
    nombre= models.CharField(max_length=30)
    año= models.IntegerField()

    
    def __str__(self):
     return f" nombre: {self.nombre} --- año: {self.año}"
    

class Dueño(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    domicilio= models.CharField(max_length=300)

    
    def __str__(self):
     return f" nombre: {self.nombre} --- apellido: {self.apellido} --- email: {self.email} --- domicilio: {self.domicilio}"

class Repuesto(models.Model):
    nombre= models.CharField(max_length=30)
    precio = models.IntegerField()  
    disponibilidad = models.BooleanField()

    def __str__(self):
     return f" nombre: {self.nombre} --- precio: {self.precio} --- disponibilidad: {self.disponibilidad} "

from django.contrib.auth.models import User

class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

