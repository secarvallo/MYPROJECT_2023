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

]   