from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MarcaFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    nacionalidad = forms.CharField(max_length=40)

class ModeloFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    año= forms.IntegerField()


class DueñoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    domicilio= forms.CharField(max_length=300)


class RepuestoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    precio = forms.IntegerField() 
    disponibilidad = forms.BooleanField()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
