
from django.db import models
from django.utils.translation import gettext_lazy as _
from estudiantes.models import Usuario,Estudiante

# Create your models here.
class ReciboPension (models.Model):
    mesPagado=models.CharField(max_length=2, verbose_name="Mes Pagado")
    valorP_M=models.CharField(max_length=20, verbose_name='Valor Pensión Mensual')
    fechaP_R_P=models.DateTimeField(max_length=10, verbose_name="Fecha De Pago De Recibo Pensión") #LO CONSULTÉ
    fechaE_R=models.DateTimeField(max_length=10, verbose_name="Fecha De Emisión De Recibo") #LO CONSULTÉ
    numeroPension=models.SmallIntegerField(verbose_name="Número Pensión") #LO CONSULTÉ
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")



class PazySalvo (models.Model):
    total=models.CharField(max_length=30, verbose_name="Total Cancelado Por Año")
    fecha=models.DateTimeField(max_length=10, verbose_name="Fecha de Generación paz y salvo")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    ReciboPension=models.ForeignKey(ReciboPension,on_delete=models.CASCADE,verbose_name="Recibo Pensión")

class AñoLectivo(models.Model):
    fechaInicio=models.DateTimeField(max_length=10, verbose_name="Fecha Inicio")
    fechaFin=models.DateTimeField(max_length=10, verbose_name="Fecha Fin")
    nombre=models.SmallIntegerField(verbose_name="Nombre Del Año Lectivo") #LO CONSULTÉ
    


class ReciboMatricula (models.Model):
    valor=models.CharField(max_length=20, verbose_name="Valor de Matrícula por Año")
    fechaMatricula=models.DateTimeField(max_length=10, verbose_name="Fecha de Matrícula")
    fechaP_M=models.DateTimeField(max_length=10, verbose_name="Fecha de Pago de Matrícula")
    estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE,verbose_name="Estudiante")
    anioLectivo=models.ForeignKey(AñoLectivo,on_delete=models.CASCADE,verbose_name="Año Lectivo")
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name="Usuario")






    

    
