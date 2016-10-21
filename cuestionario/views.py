from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cuestionario.models import Seccion, Pregunta
from cuestionario.serializers import SeccionSerializer, PreguntaSerializer, RespuestaSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def seccion_list(request):
    """
    Lista todas las secciones o crea una nueva(crear una nueva aún no esta terminada)
    """
    if request.method == 'GET':
        secciones = Seccion.objects.all()
        serializer = SeccionSerializer(secciones, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SeccionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def pregunta_list(request):
    """
    Lista todas las secciones o crea una nueva(crear una nueva aún no esta terminada)
    """
    if request.method == 'GET':
        preguntas = Pregunta.objects.all()
        serializer = PreguntaSerializer(preguntas, many=True)
        return JSONResponse(serializer.data)

    # elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = SeccionSerializer(data=data)
        # if serializer.is_valid():
            # serializer.save()
            # return JSONResponse(serializer.data, status=201)
        # return JSONResponse(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def respuesta_post(request):
    """
    Guarda las respuestas
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RespuestaSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

