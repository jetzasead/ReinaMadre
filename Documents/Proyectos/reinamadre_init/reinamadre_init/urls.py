"""reinamadre_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import login, logout
from aplicaciones.principal.views import inicio,crearEmpleado,editarEmpleado,eliminarEmpleado,buscar
from aplicaciones.principal.class_view import EmpleadoList,EmpleadoCreate,EmpleadoUpdate,EmpleadoDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name="login"),
    path('lista_empleado/',buscar,name="lista_empleado"),
    path('crear_empleado/',EmpleadoCreate.as_view(),name="crear_empleado"),
    path('editar_empleado/<int:pk>/',EmpleadoUpdate.as_view(),name="editar_empleado"),
    path('eliminar_empleado/<int:pk>/',EmpleadoDelete.as_view(),name="eliminar_empleado"),




]
