from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),# INDEX
    path('servicios', views.servicios, name="servicios"),#SERVICIOS
    path('precios', views.precios, name="precios"),#PRECIOS
    path('contacto', views.contacto, name="contacto"),#CONTACTO
    path('servicioCliente', views.sCliente, name="sCliente"),#SERVIOS AL CLIENTE
    path('identity', views.identity, name="identity"),#IDENTITY

    path('formulario', views.formulario, name="formulario"),
]