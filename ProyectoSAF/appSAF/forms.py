from django import forms
from django.shortcuts import render

class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=20, required=True, label="Marca") # campo requerido
    modelo = forms.CharField(max_length=20, required=True, label="Modelo") # campo requerido
    matricula = forms.CharField(max_length=20, required=True, label="Matricula") # campo requerido 

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True, label="Nombre") # campo requerido
    apellido = forms.CharField(max_length=60, required=True, label="Apellido") # campo requerido
    email = forms.EmailField(required=True) # campo requerido
    direccion = forms.CharField(max_length=100, required=True, label="Dirección") # campo requerido

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True, label="Nombre") # campo requerido
    apellido = forms.CharField(max_length=60, required=True, label="Apellido") # campo requerido
    email = forms.EmailField(required=True) # campo requerido

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True, label="Nombre") # campo requerido
    apellido = forms.CharField(max_length=60, required=True, label="Apellido") # campo requerido
    documento = forms.CharField(max_length=20, required=True, label="Documento") # campo requerido