from django.db import models

# Create your models here.
class Empresa(models.Model):


    IdEmpresa= models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre
 
class Departamento(models.Model):

    IdDepartamento= models.AutoField(primary_key=True)
    IdEmpresaFk=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Nombre=models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre
 


class Empleado(models.Model):

    IdEmpleado= models.AutoField(primary_key=True)
    IdEmpresafk= models.ForeignKey(Empresa, on_delete=models.CASCADE)
    IdDepartamentofk= models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Nombre=models.CharField(max_length=200)
    ApPaterno=models.CharField(max_length=200)
    ApMaterno=models.CharField(max_length=200)
    FechaNac=models.DateField()
    Email=models.EmailField()
    Genero=models.CharField(max_length=1,  null=True)
    TelCasa=models.IntegerField( null=True)
    TelCell=models.IntegerField( null=True)
    FechaIngreso=models.DateField()

    def __str__(self):
        return self.Nombre

  