from django.contrib import admin
from cuestionario.models import Seccion, Subseccion, Pregunta, Respuesta

# Register your models here.
admin.site.register(Seccion)
admin.site.register(Subseccion)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
