
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Grado (models.Model):
    nombre=models.CharField(max_length=60, verbose_name="Nombre")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
class Usuario (models.Model):
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        PP='P.P', _('Permiso Especial')
        TI='T.I', _('Tarjeta de Identidad')
        RC='R.C', _('Registro Civil' )
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=6, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")
    fechaNacimiento=models.DateField(verbose_name="fecha de nacimiento", help_text=u"MM/DD/AAAA")
    email=models.CharField(max_length=100, verbose_name="Email")
    contrasena=models.CharField(max_length=60, verbose_name="Contraseña")
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
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=20, verbose_name="Número de Documento")
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")
    fechaNacimiento=models.DateField(verbose_name="fecha de nacimiento", help_text=u"MM/DD/AAAA")
    edad=models.SmallIntegerField(verbose_name="Edad") #LO CONSULTÉ
    genero=models.CharField(max_length=60, verbose_name="Género")
    direccionResidencia=models.CharField(max_length=70, verbose_name="Dirección Residencia")
    celularEstudiante=models.CharField(max_length=20, verbose_name="Celular Estudiante")
    colegio=models.CharField(max_length=100, verbose_name="Colegio Anterior Cuidad")
    nombreC_E=models.CharField(max_length=100, verbose_name="Nombre Celular Emergencia")
    nombreAcudiente=models.CharField(max_length=60, verbose_name="Nombre Acudiente")
    numeroC_A=models.CharField(max_length=20, verbose_name="Número Celular Acudiente")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    grado=models.ForeignKey(Grado,on_delete=models.CASCADE,verbose_name="Grado")
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name="Usuario")      



