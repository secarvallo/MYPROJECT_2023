from django.shortcuts import render
from django.http import HttpResponse
from .models import Forms


# Create your views here.

def index(request):
    return render(request, "rayoMakween/index.html")
def servicios(request):
    return render(request, "rayoMakween/servicios.html")
def precios(request):
    return render(request, "rayoMakween/precios.html")
def contacto(request):
    return render(request, "rayoMakween/contacto.html")
def sCliente(request):
    return render(request, "rayoMakween/servicio_cliente.html")
def identity(request):
    return render(request, "rayoMakween/identity.html")

def formulario(request):
    return render(request, "rayoMakween/formulario.html")

def base(request):
    Form= Forms.objects.all()
    return render(request, "rayoMakween/base.html", {"forms": Form})