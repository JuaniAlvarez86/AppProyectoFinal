from django.urls import path

from AppProyectoFinal import views

from django.contrib.auth.views import LogoutView 





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('marcas', views.marcas, name="Marcas"),
    path('modelos', views.modelos, name="Modelos"),
    path('dueños', views.dueños, name="Dueños"),
    path('repuestos', views.repuestos, name="Repuestos"),
    path('marcaFormulario', views.marcaFormulario, name="MarcaFormulario"),
    path('modeloFormulario', views.modeloFormulario, name="ModeloFormulario"),
    path('dueñoFormulario', views.dueñoFormulario, name="DueñoFormulario"),
    path('repuestoFormulario', views.repuestoFormulario, name="RepuestoFormulario"),
    path('busquedaRepuesto', views.busquedaRepuesto, name="BusquedaRepuesto"),
    path('buscar/', views.buscar),
    path('leerMarcas', views.leerMarcas, name = "LeerMarcas"),
    path('leerModelos', views.leerModelos, name = "LeerModelos"),
    path('leerRepuestos', views.leerRepuestos, name = "LeerRepuestos"),
    path('leerDueños', views.leerDueños, name = "LeerDueños"),
    path('eliminarRepuesto/<repuesto_nombre>/', views.eliminarRepuesto, name="EliminarRepuesto"),
    path('eliminarDueño/<dueño_nombre>/', views.eliminarDueño, name="EliminarDueño"),
    path('eliminarMarca/<marca_nombre>/', views.eliminarMarca, name="EliminarMarca"),
    path('eliminarModelo/<modelo_nombre>/', views.eliminarModelo, name="EliminarModelo"),
    path('editarDueño/<dueño_nombre>/', views.editarDueño, name="EditarDueño"),
    path('editarRepuesto/<repuesto_nombre>/', views.editarRepuesto, name="EditarRepuesto"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppProyectoFinal/logout.html'), name="Logout"),

]

