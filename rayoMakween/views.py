from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .models import Formulario
# Create your views here.
#----------------------------------------------------> Templates
def index(request):
    return render(request, "rayoMakween/index.html")
def servicios(request):
    return render(request, "rayoMakween/servicios.html")
def contacto(request):
    f = Formulario.objects.all()
    return render(request, "rayoMakween/contacto.html", {'formularios':f})
def sCliente(request):
    return render(request, "rayoMakween/servicio_cliente.html")
def identity(request):
    return render(request, "rayoMakween/identity.html")
#------------------------------------------------------> 

#------------------------------------------------------> 
def regForms(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    celular = request.POST['numCelular']
    servicios = request.POST['txtServicios']
    comentario = request.POST['txtComentario']
    Form= Formulario.objects.create(nombre=nombre, apellido=apellido, email=email , celular=celular, servicios=servicios, comentario=comentario)
    return redirect('/')

#------------------------------------------------------>
@login_required
def precios(request):
    return render(request, "rayoMakween/precios.html")

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('index')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)
#------------------------------------------------------>