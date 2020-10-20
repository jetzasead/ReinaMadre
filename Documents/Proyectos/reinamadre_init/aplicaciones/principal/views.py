from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .models import Empleado,Departamento
from .forms import EmpleadoForm
from django.db.models import Q
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect







# Create your views here.

def inicio(request):
    empleados = Empleado.objects.all()
    
    contexto = {
        'empleados':empleados
    }
    return render(request,'index.html',contexto)


def crearEmpleado(request):
    if request.method == "GET":
        form = EmpleadoForm()
        contexto = {
            'form':form
        }
    else:
        form= EmpleadoForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_empleado.html',contexto)


def editarEmpleado(request,IdEmpleado):
    empleado= Empleado.objects.get(IdEmpleado=IdEmpleado)
    if request.method == 'GET':
        form = EmpleadoForm(instance=empleado)
        contexto = {
            'form':form
        }
    else:
        form= EmpleadoForm(request.POST, instance = empleado)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_empleado.html',contexto)    
     
def eliminarEmpleado(request,IdEmpleado):
    empleado= Empleado.objects.get(IdEmpleado=IdEmpleado)
    empleado.delete()
    return redirect('index')


def buscar(request):
    busqueda = request.POST.get("buscar")
    empleados = Empleado.objects.all()
    departamentos= Departamento.objects.all()

    if busqueda:
        empleados=Empleado.objects.filter(
                    Q(Nombre__icontains = busqueda) 
        ).distinct()

    if busqueda:
         departamentos=Departamento.objects.filter(
                    Q(Nombre__icontains = busqueda)
        ).distinct()
 

       
    
    
      

    return render(request,'empleados.html',{'empleados':empleados})



