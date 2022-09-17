from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Modelo)

admin.site.register(Repuesto)

admin.site.register(Dueño)

admin.site.register(Marca)
