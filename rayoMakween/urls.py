from django.urls import path
from . import views

urlpatterns = [
    #----------------------------------------------------> Templates
    path('', views.index, name="index"),# INDEX
    path('servicios', views.servicios, name="servicios"),#SERVICIOS
    path('precios', views.precios, name="precios"),#PRECIOS
    path('contacto', views.contacto, name="contacto"),#CONTACTO
    path('servicioCliente', views.sCliente, name="sCliente"),#SERVIOS AL CLIENTE
    path('identity', views.identity, name="identity"),#IDENTITY
    #----------------------------------------------------> 
    path('regForms', views.regForms, name='regForms'),#REGISTRO DE FORMULARIO
    path('register', views.register, name='register'),#REGISTRO DE FORMULARIO
    #----------------------------------------------------> 
    path('crear/',views.crear,name='crear'),
    path('eliminar/',views.eliminar,name='eliminar'),
    path('modificar',views.modificar,name='modificar'),
    #path('registrar/',views.registrar,name='registrar'),---->registrar
    path('mostrar/',views.mostrar,name='mostrar'),


    path('tienda/',views.tienda,name='tienda'),
    path('tienda/',views.tienda,name='tienda'),
    path('generarBoleta/',views.generarBoleta,name='generarBoleta'),
    path('agregar/<id>',views.agregar_producto,name='agregar'),
    path('eliminar/<id>',views.eliminar_producto,name='eliminar_producto'),
    path('restar/<id>',views.restar_producto, name='restar'),
    path('limpiar/',views.limpiar_carrito,name='limpiar')

]   