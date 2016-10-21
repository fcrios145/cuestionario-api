# serializers

from rest_framework import serializers
from cuestionario.models import Pregunta, Seccion, Subseccion, Respuesta

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subseccion
        fields = ('id', 'nombre')


class SubseccionSerializer(serializers.ModelSerializer):
    seccion = SeccionSerializer(many=False)
    class Meta:
        model = Pregunta
        depth = 1
        fields = ('id', 'nombre', 'seccion')

class PreguntaSerializer(serializers.ModelSerializer):
    subseccion = serializers.CharField(source='subseccion.nombre')
    seccion = serializers.CharField(source='subseccion.seccion.nombre')

    seccion_id = serializers.IntegerField(source='subseccion.seccion.id')
    subseccion_id = serializers.CharField(source='subseccion.id')
    valor = serializers.IntegerField(default=1);
    class Meta:
        model = Pregunta
        fields = ('id', 'nombre', 'subseccion', 'seccion', 'valor', 'subseccion_id', 'seccion_id')

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ('pregunta', 'valor')
