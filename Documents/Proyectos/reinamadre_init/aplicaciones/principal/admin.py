from django.contrib import admin
from .models import  Empresa
from .models import Departamento
from .models import Empleado
admin.site.register(Empresa)
admin.site.register(Departamento)
admin.site.register(Empleado)
# Register your models here.
