from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Empresa
from .serializers import EmpresaSerializer

class EmpresaListCreateAPIView(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import generics
from .models import TipoEnvio
from .serializers import TipoEnvioSerializer

class TipoEnvioListCreate(generics.ListCreateAPIView):
    queryset = TipoEnvio.objects.all()
    serializer_class = TipoEnvioSerializer


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Responsable
from .serializers import ResponsableSerializer

@api_view(['GET', 'POST'])
def responsable_list(request):
    if request.method == 'GET':
        responsables = Responsable.objects.all()
        serializer = ResponsableSerializer(responsables, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ResponsableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def responsable_detail(request, pk):
    try:
        responsable = Responsable.objects.get(pk=pk)
    except Responsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ResponsableSerializer(responsable)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ResponsableSerializer(responsable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        responsable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Planilla
from .serializers import PlanillaSerializer

class PlanillaAPIView(APIView):
    def get(self, request):
        planillas = Planilla.objects.all()
        serializer = PlanillaSerializer(planillas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanillaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        planilla = Planilla.objects.get(idplanilla=id)
        serializer = PlanillaSerializer(planilla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        planilla = Planilla.objects.get(idplanilla=id)
        planilla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Emisor
from .serializers import EmisorSerializer

class EmisorListCreateAPIView(APIView):
    def get(self, request):
        emisor = Emisor.objects.all()
        serializer = EmisorSerializer(emisor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Especie
from .serializers import EspecieSerializer

class EspecieListCreateAPIView(APIView):
    def get(self, request):
        especie = Especie.objects.all()
        serializer = EspecieSerializer(especie, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EspecieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Turno
from .serializers import TurnoSerializer

class TurnoListCreateAPIView(APIView):
    def get(self, request):
        turno = Turno.objects.all()
        serializer = TurnoSerializer(turno, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Consumidor
from .serializers import ConsumidorSerializer

class ConsumidorListCreateAPIView(APIView):
    def get(self, request):
        consumidor = Consumidor.objects.all()
        serializer = ConsumidorSerializer(consumidor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConsumidorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import ImportarAsistencia, EstadoDia
from .serializers import ImportarAsistenciaSerializer

@api_view(['POST'])
def importar_asistencia_list(request):
    if request.method == 'POST':
        # Obtener la fecha actual en tiempo real en formato YYYYMMDD
        fecha_actual = timezone.now().strftime('%Y%m%d')

        # Verificar si el día está abierto
        estado = EstadoDia.determinar_estado(fecha_actual)
        if not estado:
            return Response({"error": "El día está cerrado. No se pueden importar asistencias en este momento."},
                            status=status.HTTP_403_FORBIDDEN)

        idcodigogeneral = request.data.get('idcodigogeneral')

        # Verificar si ya existe un registro para idcodigogeneral en la fecha actual
        existing_importaciones = ImportarAsistencia.objects.filter(idcodigogeneral=idcodigogeneral, fecha=fecha_actual)
        if existing_importaciones.exists():
            return Response({"error": "Ya se ha importado la asistencia para este idcodigogeneral hoy."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = ImportarAsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def importar_asistencia_detail_by_idcodigogeneral(request, idcodigogeneral):
    try:
        importar_asistencia = ImportarAsistencia.objects.get(idcodigogeneral=idcodigogeneral)
    except ImportarAsistencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Verificar si el día está abierto
    estado = EstadoDia.determinar_estado(timezone.now().date())
    if not estado:
        return Response({"error": "El día está cerrado. No se pueden realizar operaciones en las asistencias."},
                        status=status.HTTP_403_FORBIDDEN)

    # Verificar si el objeto está en los datos ingresados hoy
    fecha_hoy = timezone.now().strftime('%Y%m%d')
    if not ImportarAsistencia.objects.filter(fecha=fecha_hoy, idcodigogeneral=idcodigogeneral).exists():
        return Response({"error": "El objeto no existe en los datos ingresados hoy."},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImportarAsistenciaSerializer(importar_asistencia)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = ImportarAsistenciaSerializer(importar_asistencia, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        importar_asistencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ------------------------------------------------------------------------------------

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImportarAsistencia
from .serializers import AsistenciaSerializer

class POTAAsistenciaUpdateByCodigoGeneralView(APIView):
    def get(self, request, codigo_general=None):
        # Verificar si el día está abierto
        estado = EstadoDia.determinar_estado(timezone.now().date())
        if not estado:
            return Response({"error": "El día está cerrado. No se pueden realizar operaciones en las asistencias."},
                            status=status.HTTP_403_FORBIDDEN)

        if codigo_general is not None:
            try:
                asistencia = ImportarAsistencia.objects.get(idcodigogeneral=codigo_general)
                serializer = AsistenciaSerializer(asistencia)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ImportarAsistencia.DoesNotExist:
                return Response({'error': 'Asistencia no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        else:
            importar_asistencias = ImportarAsistencia.objects.all()
            serializer = AsistenciaSerializer(importar_asistencias, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, codigo_general):
        # Verificar si el día está abierto
        estado = EstadoDia.determinar_estado(timezone.now().date())
        if not estado:
            return Response({"error": "El día está cerrado. No se pueden realizar operaciones en las asistencias."},
                            status=status.HTTP_403_FORBIDDEN)

        # Verificar si el objeto está en los datos ingresados hoy
        fecha_hoy = timezone.now().strftime('%Y%m%d')
        if not ImportarAsistencia.objects.filter(fecha=fecha_hoy, idcodigogeneral=codigo_general).exists():
            return Response({"error": "El objeto no existe en los datos ingresados hoy."},
                            status=status.HTTP_404_NOT_FOUND)

        try:
            asistencia = ImportarAsistencia.objects.get(idcodigogeneral=codigo_general)
            serializer = AsistenciaSerializer(asistencia, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(update_fields=['cantidad'])
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ImportarAsistencia.DoesNotExist:
            return Response({'error': 'Asistencia no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def actualizarImportarAsistencia(self, codigo_general, data):
        # Verificar si el día está abierto
        estado = EstadoDia.determinar_estado(timezone.now().date())
        if not estado:
            return False, {"error": "El día está cerrado. No se pueden realizar operaciones en las asistencias."}

        try:
            asistencia = ImportarAsistencia.objects.get(idcodigogeneral=codigo_general)
            serializer = AsistenciaSerializer(asistencia, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(update_fields=['cantidad'])
                return True, serializer.data
            return False, serializer.errors
        except ImportarAsistencia.DoesNotExist:
            return False, {'error': 'Asistencia no encontrada'}


#---------------------------------------------------
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EstadoDia
from .serializers import EstadoDiaSerializer
from django.utils import timezone
from datetime import datetime


@api_view(['POST'])
def estado_dia(request):
    if request.method == 'POST':
        # Obtener la fecha actual en formato YYYY-MM-DD
        fecha_actual = datetime.now().date()

        # Verificar si ya existe un registro para la fecha actual
        if EstadoDia.objects.filter(fecha=fecha_actual).exists():
            return Response({"error": "El día ya está abierto."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Crear un nuevo registro para la fecha actual
        estado = EstadoDia.objects.create(fecha=fecha_actual, abierto=True)
        return Response({"message": "El día se ha abierto correctamente."},
                        status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def cerrar_dia(request, fecha):
    try:
        fecha = datetime.strptime(fecha, '%Y-%m-%d').date()  # Convertir la fecha a un objeto datetime.date
        estado = EstadoDia.objects.get(fecha=fecha)
    except EstadoDia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Verificar si el día ya está cerrado
    if estado.hora_cierre is not None:
        return Response({"message": "El día ya está cerrado"}, status=status.HTTP_400_BAD_REQUEST)

    estado.cerrar_dia()
    serializer = EstadoDiaSerializer(estado)
    return Response(serializer.data)




from django.http import JsonResponse
from django.utils import timezone
from .models import ImportarAsistencia, EstadoDia

def vista_datos_ingresados_hoy(request):
    fecha_hoy = timezone.now().strftime('%Y%m%d')  # Formato '20240220'
    estado_dia_hoy = EstadoDia.objects.filter(fecha=fecha_hoy).first()

    # Mostrar los datos ingresados hoy independientemente del estado del día
    datos_ingresados_hoy = ImportarAsistencia.objects.filter(fecha=fecha_hoy)
    serialized_data = [{'idempresa': registro.idempresa, 'tipo_envio': registro.tipo_envio, 'idresponsable': registro.idresponsable, 'idplanilla': registro.idplanilla, 'idemisor': registro.idemisor, 'idturno': registro.idturno, 'fecha': registro.fecha, 'idsucursal': registro.idsucursal, 'item': registro.item, 'idcodigogeneral': registro.idcodigogeneral, 'idactividad': registro.idactividad, 'idlabor': registro.idlabor, 'idconsumidor': registro.idconsumidor, 'cantidad': registro.cantidad, 'idespecie': registro.idespecie} for registro in datos_ingresados_hoy]
    
    return JsonResponse({'datos': serialized_data})
