import json

from django.core.files import File
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from datetime import datetime
from django.db.models import Sum

#permisos
from api.permission.maestro import IsMaestroUser

#models
from api.models import Tarea

#serializer
from api.serializers import TareaSerializer, TareaReadSerializer

class TareaViewset(viewsets.ModelViewSet):
    """Viewset de tareas"""
    now = datetime.now()
    anio = now.strftime("%Y")
    queryset = Tarea.objects.filter(activo=True, asignacion__asignacion_ciclo__anio = anio)

    def get_serializer_class(self):
        """Define el serializador a utilizar"""
        if self.action == "list" or self.action == "retrieve":
            return TareaReadSerializer
        else:
            return TareaSerializer

    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated, IsMaestroUser]
        return [permission() for permission in permission_classes]

    def create(self, request):
        try:
            data = request.data
            archivo = data.get("archivo")
            data = json.loads(data["data"])
            serializer =  TareaSerializer(data=data)
            #import pdb; pdb.set_trace()
            if serializer.is_valid(raise_exception=True):
                #verifica que el punteo total de nota no exceda de 100pts
                max_nota = 100
                suma_nota = Tarea.objects.filter(
                    asignacion_id=data.get("asignacion"), 
                    asignacion__asignacion_ciclo__anio=self.anio).aggregate(Sum('nota')
                    )
                suma_total = suma_nota.get('nota__sum')
                if not suma_total:
                    suma_total=0

                if (suma_total + float(data.get("nota"))) > max_nota:
                    return Response(
                        {"detail":"Se ha excedido el valor de la nota total de este curso"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )

                if not data.get("permitir_archivo"):
                    permitir_archivo = False
                else:
                    permitir_archivo = True

                Tarea.objects.create(
                titulo=data.get("titulo"),
                descripcion=data.get("descripcion"),
                fecha_entrega=data.get("fecha_entrega"),
                hora_entrega=data.get("hora_entrega"),
                nota=data.get("nota"),
                permitir_archivo=permitir_archivo,
                archivo=File(archivo),
                asignacion_id=data.get("asignacion")
            )
            return Response('todo anda bien', status=status.HTTP_201_CREATED)
        except TypeError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['get'], detail=False)
    def asignacion(self, request):
        asignacion_id = request.query_params.get("id")
        tareas = Tarea.objects.filter(asignacion_id=asignacion_id)
        serializer = TareaReadSerializer(tareas, many=True)
        return Response(
            {"tareas" : serializer.data,}, 
            status=status.HTTP_200_OK
        )
