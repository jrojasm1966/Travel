from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from login import models as login_models
import re
import bcrypt


# Create your models here.
class TravelManager(models.Manager):
    def basic_validator(self, postData):
        errores = {}
        if len(postData['destino']) == 0:
            errores['nombre'] = "Destino es obligatorio"
        if len(postData['descripcion']) == 0:
            errores['nombre'] = "Destino es obligatorio"
        if len(postData['fechades']) == 0:
            errores['nombre'] = "Destino es obligatorio"
        if len(postData['fechahas']) == 0:
            errores['nombre'] = "Destino es obligatorio"
        return errores

class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    destino = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    fechaDesde = models.DateField()
    fechaHasta = models.DateField()
    estado = models.IntegerField()
    usuario=models.ForeignKey(login_models.User, related_name="usuario", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()
    
