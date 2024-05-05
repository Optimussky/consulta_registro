from django.db import models

class CatalogoDelito(models.Model):
    #id = models.IntegerField(primary_key=True)
    delito = models.CharField(max_length=255)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        ordering = ["-fechaCreacion"]
        verbose_name = "Delito"
        verbose_name_plural =("Delitos")

    def __str__(self):
        return self.delito

class CatalogoPersona(models.Model):
    #id = models.IntegerField(primary_key=True)
    tipo_persona = models.CharField(max_length=255)
    id_catalogoDelito = models.ForeignKey(CatalogoDelito, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        ordering = ["-fechaCreacion"]
        verbose_name = "Tipo persona"
        verbose_name_plural = "Tipo personas"

    def __str__(self):
        return self.tipo_persona

class RegistroDelitos(models.Model):
    #id = models.IntegerField(primary_key=True)
    registro = models.CharField(max_length=255, null=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateField(auto_now=True)
    delito = models.ForeignKey(CatalogoDelito, on_delete=models.CASCADE)
    tipo_persona = models.ForeignKey(CatalogoPersona, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-fechaCreacion"]
        verbose_name = "Registro"
        verbose_name_plural = "Registros"


    def __str__(self):
        return self.registro
