from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from AppProyectoFinal.models import Marca, Modelo, Repuesto, Dueño


# Create your views here.




def inicio(request):

      return render(request, "AppProyectoFinal/inicio.html")

def marcas(request):

      return render(request, "AppProyectoFinal/marcas.html")

def modelos(request):

      return render(request, "AppProyectoFinal/modelos.html")


def dueños(request):

      return render(request, "AppProyectoFinal/dueños.html")


def repuestos(request):

      return render(request, "AppProyectoFinal/repuestos.html")





from AppProyectoFinal.forms import MarcaFormulario, ModeloFormulario, RepuestoFormulario, DueñoFormulario



def marcaFormulario(request):
  if request.method == "POST":
      miFormulario = MarcaFormulario(request.POST) # Aqui me llega la informacion del html

      print(miFormulario)

      if miFormulario.is_valid:
         informacion = miFormulario.cleaned_data
         marca = Marca(nombre=informacion["nombre"], nacionalidad=informacion["nacionalidad"])
         marca.save()
      return render(request, "AppProyectoFinal/inicio.html")

  else:
      miFormulario = MarcaFormulario()
      return render(request, "AppProyectoFinal/marcaFormulario.html", {"miFormulario": miFormulario})




def modeloFormulario(request):
  if request.method == "POST":
      miFormulario1 = ModeloFormulario(request.POST) # Aqui me llega la informacion del html

      print(miFormulario1)

      if miFormulario1.is_valid:
         informacion = miFormulario1.cleaned_data
         modelo = Modelo(nombre=informacion["nombre"], año=informacion["año"])
         modelo.save()
      return render(request, "AppProyectoFinal/inicio.html")

  else:
      miFormulario1 = ModeloFormulario()
      return render(request, "AppProyectoFinal/modeloFormulario.html", {"miFormulario1": miFormulario1})

def dueñoFormulario(request):
  if request.method == "POST":
      miFormulario2 = DueñoFormulario(request.POST) # Aqui me llega la informacion del html

      print(miFormulario2)

      if miFormulario2.is_valid:
         informacion = miFormulario2.cleaned_data
         dueño = Dueño(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],domicilio=informacion["domicilio"])
         dueño.save()
      return render(request, "AppProyectoFinal/inicio.html")

  else:
      miFormulario2 = DueñoFormulario()
      return render(request, "AppProyectoFinal/dueñoFormulario.html", {"miFormulario2": miFormulario2})


def repuestoFormulario(request):
  if request.method == "POST":
      miFormulario3 = RepuestoFormulario(request.POST) # Aqui me llega la informacion del html

      print(miFormulario3)

      if miFormulario3.is_valid:
         informacion = miFormulario3.cleaned_data
         repuesto = Repuesto(nombre=informacion["nombre"],disponibilidad=informacion["disponibilidad"],precio=informacion["precio"])
         repuesto.save()
      return render(request, "AppProyectoFinal/inicio.html")

  else:
      miFormulario3 = RepuestoFormulario()
      return render(request, "AppProyectoFinal/repuestoFormulario.html", {"miFormulario3": miFormulario3})


def busquedaRepuesto(request):
      return render(request, "AppProyectoFinal/busquedaRepuesto.html")

def buscar(request):

      if request.GET["nombre"]:

       
       rep= request.GET["nombre"]
       repuesto= Repuesto.objects.filter(nombre__icontains=rep)
       return render(request, "resultadosRepuestos.html", {"repuesto":repuesto,"query":rep})

      else:

        respuesta = "Ingrese un nombre de producto"

      return HttpResponse(respuesta)




def leerMarcas(request):

      marcas = Marca.objects.all() 

      contexto= {"marcas":marcas} 

      return render(request, "AppProyectoFinal/leerMarcas.html",contexto)

def leerModelos(request):

      modelos = Modelo.objects.all() 

      contexto= {"modelos":modelos} 

      return render(request, "AppProyectoFinal/leerModelos.html",contexto)

def leerRepuestos(request):

      repuestos = Repuesto.objects.all() 

      contexto= {"repuestos":repuestos} 

      return render(request, "AppProyectoFinal/leerRepuestos.html",contexto)

def leerDueños(request):

      dueños = Dueño.objects.all() 

      contexto= {"dueños":dueños} 

      return render(request, "AppProyectoFinal/leerDueños.html",contexto)



def eliminarRepuesto(request, repuesto_nombre):

    repuesto = Repuesto.objects.get(nombre=repuesto_nombre)
    repuesto.delete()

   
    repuestos= Repuesto.objects.all() 

    contexto= {"repuestos":repuestos} 

    return render(request, "AppProyectoFinal/leerRepuestos.html",contexto)



def eliminarDueño(request, dueño_nombre):

    dueño = Dueño.objects.get(nombre=dueño_nombre)
    dueño.delete()

   
    dueños= Dueño.objects.all() 

    contexto= {"dueños":dueños} 

    return render(request, "AppProyectoFinal/leerDueños.html",contexto)




def eliminarMarca(request, marca_nombre):

    marca = Marca.objects.get(nombre=marca_nombre)
    marca.delete()

   
    marcas= Marca.objects.all() 

    contexto= {"marcas":marcas} 

    return render(request, "AppProyectoFinal/leerMarcas.html",contexto)


def eliminarModelo(request, modelo_nombre):

    modelo = Modelo.objects.get(nombre=modelo_nombre)
    modelo.delete()

   
    modelo= Modelo.objects.all() 

    contexto= {"modelos":modelos} 

    return render(request, "AppProyectoFinal/leerModelos.html",contexto)


def editarDueño(request, dueño_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    dueño = Dueño.objects.get(nombre=dueño_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = DueñoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            dueño.nombre = informacion['nombre']
            dueño.apellido = informacion['apellido']
            dueño.email = informacion['email']
            dueño.domicilio = informacion['domicilio']

            dueño.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppProyectoFinal/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = DueñoFormulario(initial={'nombre': dueño.nombre, 'apellido': dueño.apellido,
                                                   'email': dueño.email, 'domicilio': dueño.domicilio})

    # Voy al html que me permite editar
    return render(request, "AppProyectoFinal/editarDueño.html", {"miFormulario": miFormulario, "dueño_nombre": dueño_nombre})

def editarRepuesto(request, repuesto_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    repuesto = Repuesto.objects.get(nombre=repuesto_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = RepuestoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            repuesto.nombre = informacion['nombre']
            repuesto.precio = informacion['precio']
            repuesto.disponibilidad = informacion['disponibilidad']
            

            repuesto.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppProyectoFinal/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = RepuestoFormulario(initial={'nombre': repuesto.nombre, 'precio': repuesto.precio,
                                                   'disponibilidad': repuesto.disponibilidad})

    # Voy al html que me permite editar
    return render(request, "AppProyectoFinal/editarRepuesto.html", {"miFormulario": miFormulario, "repuesto_nombre": repuesto_nombre})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

#Para el login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate




def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppProyectoFinal/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppProyectoFinal", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppProyectoFinal/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppProyectoFinal/login.html", {'form':form} )

from AppProyectoFinal.forms import UserRegisterForm, UserEditForm

def register(request):

 if request.method == 'POST':

  #form = UserCreationForm(request.POST)
  form = UserRegisterForm(request.POST)

  if form.is_valid():

      username = form.cleaned_data['username']
      form.save()
      return render(request,"AppProyectoFinal/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


 else:
    #form = UserCreationForm()       
    form = UserRegisterForm()     

 return render(request,"AppProyectoFinal/registro.html" ,  {"form":form})


def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppProyectoFinal/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppProyectoFinal/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


def nosotros(request):

      return render(request, "AppProyectoFinal/nosotros.html")
