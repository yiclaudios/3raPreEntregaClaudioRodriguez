from .views import *
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return(render(request, "entidades/index.html"))

def vehiculos(request):
    contexto = {"vehiculos" : Vehiculo.objects.all()}
    return(render(request, "entidades/vehiculos.html", contexto))

def proveedores(request):
    contexto = {"proveedores" : Proveedor.objects.all()}
    return(render(request, "entidades/proveedores.html", contexto))

def clientes(request):
    contexto = {"clientes" : Cliente.objects.all()}
    return(render(request, "entidades/clientes.html", contexto))

def empleados(request):
    contexto = {"empleados" : Empleado.objects.all()}
    return(render(request, "entidades/empleados.html", contexto))

def acerca(request):
    return(render(request, "entidades/acerca.html"))

# * * *  Formularios  * * *

def clienteForm(request):
    if (request.method == "POST"):
        miform = ClienteForm(request.POST)
        if (miform.is_valid()):
            cliente_nombre = miform.cleaned_data.get("nombre")
            cliente_apellido = miform.cleaned_data.get("apellido")
            cliente_email = miform.cleaned_data.get("email")
            cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido, email = cliente_email)
            cliente.save()
            contexto = {"clientes" : Cliente.objects.all()}
            return(render(request, "entidades/clientes.html", contexto))
    else:
        miform = ClienteForm()
    
    return(render(request, "entidades/clienteForm.html", {"form" : miform}))

def vehiculoForm(request):
    if (request.method == "POST"):
        miform = VehiculoForm(request.POST)
        if (miform.is_valid()):
            vehiculo_marca = miform.cleaned_data.get("marca")
            vehiculo_modelo = miform.cleaned_data.get("modelo")
            vehiculo_matricula = miform.cleaned_data.get("matricula")
            vehiculo = Vehiculo(marca = vehiculo_marca, modelo = vehiculo_modelo, matricula = vehiculo_matricula)
            vehiculo.save()
            contexto = {"vehiculos" : Vehiculo.objects.all()}
            return(render(request, "entidades/vehiculos.html", contexto))
    else:
        miform = VehiculoForm()
    
    return(render(request, "entidades/vehiculoForm.html", {"form" : miform}))

def proveedoresForm(request):
    if (request.method == "POST"):
        miform = ProveedorForm(request.POST)
        if (miform.is_valid()):
            proveedor_nombre = miform.cleaned_data.get("nombre")
            proveedor_apellido = miform.cleaned_data.get("apellido")
            proveedor_email = miform.cleaned_data.get("email")
            proveedor_direccion = miform.cleaned_data.get("direccion")
            proveedor = Proveedor(nombre = proveedor_nombre, 
                                  apellido = proveedor_apellido, 
                                  email = proveedor_email,
                                  direccion = proveedor_direccion)
            proveedor.save()
            contexto = {"proveedores" : Proveedor.objects.all()}
            return(render(request, "entidades/proveedores.html", contexto))
    else:
        miform = ProveedorForm()
    
    return(render(request, "entidades/proveedorForm.html", {"form" : miform}))


def empleadosForm(request):
    if (request.method == "POST"):
        miform = EmpleadoForm(request.POST)
        if (miform.is_valid()):
            empleado_nombre = miform.cleaned_data.get("nombre")
            empleado_apellido = miform.cleaned_data.get("apellido")
            empleado_documento = miform.cleaned_data.get("documento")
            empleado = Empleado(nombre = empleado_nombre, 
                                  apellido = empleado_apellido,
                                  documento = empleado_documento)
            empleado.save()
            contexto = {"empleados" : Empleado.objects.all()}
            return(render(request, "entidades/empleados.html", contexto))
    else:
        miform = EmpleadoForm()
    
    return(render(request, "entidades/empleadoForm.html", {"form" : miform}))

# Formulario de búsqueda
def buscarVehiculos(request):
    return(render(request, "entidades/buscar.html"))

def encontrarVehiculos(request):
    if (request.GET["buscar"]):
        patron = request.GET["buscar"]
        vehiculo = Vehiculo.objects.filter(matricula__icontains=patron) # devuelve lo que encuentra que contenga el patron que se le pasa
        contexto = {"vehiculos" : vehiculo }
    else:
        contexto = {"vehiculos" : Vehiculo.objects.all()}
    return render(request, "entidades/vehiculos.html", contexto)