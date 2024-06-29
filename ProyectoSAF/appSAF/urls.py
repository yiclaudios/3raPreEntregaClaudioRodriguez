from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('proveedores/', proveedores, name="proveedores"),
    path('clientes/', clientes, name="clientes"),
    path('empleados/', empleados, name="empleados"),
    path('acerca/', acerca, name="acerca"),

    ## * * *  Formularios  * * *
    path('vehiculoForm/', vehiculoForm, name="vehiculoForm"),
    path('proveedorForm/', proveedoresForm, name="proveedorForm"),
    path('buscarVehiculos/', buscarVehiculos, name="buscarVehiculos"),
    path('encontrarVehiculos/', encontrarVehiculos, name="encontrarVehiculos"),
    path('clienteForm/', clienteForm, name="clienteForm"),
    path('empleadoForm/', empleadosForm, name="empleadoForm")
]
