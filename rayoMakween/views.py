from django.shortcuts import render, redirect
from .models import formulario
from django.http import HttpResponse



# Create your views here.
#----------------------------------------------------> Templates
def index(request):
    return render(request, "rayoMakween/index.html")
def servicios(request):
    return render(request, "rayoMakween/servicios.html")
def precios(request):
    return render(request, "rayoMakween/precios.html")
def contacto(request):
    forms = formulario.objects.all()
    return render(request, "rayoMakween/contacto.html", {'formularios':forms})
def sCliente(request):
    return render(request, "rayoMakween/servicio_cliente.html")
def identity(request):
    return render(request, "rayoMakween/identity.html")
#------------------------------------------------------> 
def regForms(request):
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        email = request.POST.get['txtEmail', False]
        celular = request.POST['numCelular']
        comuna = request.POST['txtComuna']
        region = request.POST['txtRegion']
        servicios = request.POST['txtServicios']
        comentario = request.POST['txtComentario']

        formulario.objects.create(nombre=nombre, apellido=apellido, email=email, celular=celular, comuna=comuna, region=region, servicios=servicios, comentario=comentario)
        return redirect('contacto')

#------------------------------------------------------>