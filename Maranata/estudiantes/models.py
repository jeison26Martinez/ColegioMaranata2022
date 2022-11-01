from xml.dom.minidom import Document
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Grado (models.Model):
    nombre=models.CharField(max_length=60, verbose_name="Nombre")
    curso=models.CharField(max_length=60, verbose_name="Nombre")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
class Estudiante (models.Model):
    class TipoDocumento(models.TextChoices):
        RC='R.C', _('Registro Civil')
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        TI='T.I', _('Tarjeta de Identidad')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text=u"MM/DD/AAAA")
    grado=models.ForeignKey(Grado,on_delete=models.CASCADE,verbose_name="Grado")   
