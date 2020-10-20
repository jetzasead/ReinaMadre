from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import EmpleadoForm
from .models import Empleado
from django.views import generic
from django.db.models import Q




class EmpleadoList(generic.ListView):
    model= Empleado
    queryset = Empleado.objects.filter(IdEmpresafk = True)
    template_name="empleados.html"

class EmpleadoCreate(CreateView):
    model= Empleado
    form_class=EmpleadoForm
    template_name="crear_empleado.html"
    success_url= reverse_lazy('lista_empleado')

class EmpleadoUpdate(UpdateView):
    model= Empleado
    form_class=EmpleadoForm
    template_name="crear_empleado.html"
    success_url= reverse_lazy('lista_empleado')

class EmpleadoDelete(DeleteView):
    model= Empleado
    template_name="eliminar_empleado.html"
    success_url= reverse_lazy('lista_empleado')
