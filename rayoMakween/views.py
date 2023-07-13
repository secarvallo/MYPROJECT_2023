from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm #ProductoForm
from .models import Formulario 
# Create your views here.
#--------------------------------------------------->
from .models import Producto, Boleta, Detalle_boleta
from .buy import Carrito
#--------------------------------------------------->
#links templates
#----------------------------------------------------> 
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
#formulario antiguo
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
#registra usuario
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
#funciones para el carrito de compras
#VIEW DEL CRUD --FUNCIONES
#------------------------------------------------------>

#def index(request):
#	return render(request,'index')

#@login_required
def otra(request):
	lubricantes= productos.objects.raw('Select * from productos_productos')
	datos={
		'productos':lubricantes
	}
	return render(request, 'otra.html', datos)

#@login_required
def crear(request):
	if request.method== 'POST':
		productoform= ProductoForm(request.POST, request.FILES)
		if productoform.is_valid():
			productoform.save()
			return redirect('otra.html')
		else:
			productoform=ProductoForm()
		return render(request, 'crear.html',{'productoform':productoform})
	
#@login_required
def eliminar(request, id):
	productoEliminado= Producto.objects.get(codigo= id)
	productoEliminado.delete()
	return redirect('otra.html')

#@login_required
def modificar(request, id):
	productoModificado= Producto.objects.get(codigo=id)
	datos={
		'form': ProductoForm(instance= productoModificado)
	}
	if request.method=='POST':
		formulario= ProductoForm(data=request.POST, instance= vehiculoModificado)
		if formulario.is_valid():
			formulario.save()
			return redirect('otra')
	return render(request, 'modificar.html',datos)
#---------------------------------------------------------------------------------->
#funcion de registrar usuario segun clase online carrito de compras
#---------------------------------------------------------------------------------->

'''
def registrar(request):
	data={
		'form':RegistroUserForm()
	}
	if request.methof=='POST':
		formulario= RegistroUserForm(data=request.POST)
		if formulario.is_calid():
			formulario.save()
			user= authenticate(username= formulario.cleaned_data["username"],password=formulario.cleaned_data['password1'])
			login(request,user)
			return redirect('index')
		data['form']=formulario
		return render(request,'registration/registrar.html,data')
'''


def mostrar(request):
	lubricantes= Producto.objects.all()
	datos={
		'lubricantes':lubricantes
	}
	return render(request,'mostrar.html', datos)

def tienda(request):
	lubricantes= Producto.objects.all()
	datos= {
		'lubricantes':lubricantes
	}
	return render(request,'tienda.html',datos)


def agregar_producto(request,id):
	carrito_compra = Carrito(request)
	producto = producto.objects.get(patente=id)
	carrito_compra.agregar(producto = producto)
	return redirect('tienda')

def eliminar_producto(request, id):
	carrito_compra = Carrito(request)
	producto = producto.objects.get(patente=id)
	carrito_compra.eliminar(producto = producto)
	return redirect('tienda')

def restar_producto(request, id):
	carrito_compra = Carrito(request)
	producto = producto.objects.get(patente=id)
	carrito_compra.restar(producto = producto)
	return redirect('tienda')

def limpiar_carrito(request, id):
	carrito_compra = Carrito(request)
	carrito_compra.limpiar()
	return redirect('tienda')

def generarBoleta(request):
	precio_total= 0
	for key, value in request.session['carrito'].items():
		precio_total= precio_total + int(value['precio']) * int(value['cantidad'])
	boleta = Boleta(total= precio_total)
	boleta.save()
	productos= []
	for key, value in request.session['carrito'].items():
		producto= producto.objects.get(patente=value['producto_id'])
		cant= value['cantidad']
		subtotal= cant * int(value['precio'])
		detalle= Detalle_boleta(id_boleta= boleta, id_producto= producto, cantidad= cant, subtotal= subtotal)
		detalle.save()
		productos.append(detalle)
	datos={
		'productos': productos,
		'fecha': boleta.fechaCompra,
		'total': boleta.total 
	}
	request.session['boleta']= boleta.id_boleta
	carrito= Carrito(request)
	carrito.limpiar()
	return render(request,'detallecarrito.html',datos)