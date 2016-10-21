from django.db import models

# Create your models here.

class Seccion (models.Model):
    nombre = models.CharField(max_length=256)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)


class Grupo (models.Model):
    nombre = models.CharField(max_length=256)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

class Subseccion (models.Model):
    nombre = models.CharField(max_length=256)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)


class Pregunta (models.Model):
    nombre = models.CharField(max_length=512)
    valor = models.IntegerField()
    subseccion = models.ForeignKey(Subseccion, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.subseccion.seccion.nombre, self.subseccion.nombre, self.nombre)

class Respuesta (models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    valor = models.IntegerField()

    def __str__(self):
        return '%s' % (self.pregunta.nombre)


from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
