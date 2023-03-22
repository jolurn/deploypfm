from rest_framework import viewsets
from posgradofimapp.models import Matricula, Alumno, Persona, DetalleMatricula, ReporteEconomico, ReporteEcoConceptoPago, User
from posgradofimapp.serializer import DetalleMatriculaSerializer, PersonaSerializer, MatriculaSerializer, ReporteEcoConceptoPagoSerializer, AlumnoSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated


class PersonaViewsets(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def listar(self, request):
        queryset = Persona.objects.all()
        serializer = PersonaSerializer(queryset, many=True)
        return Response(serializer.data)

    def listar_persona_email(self, request, email):
        persona = Persona.objects.filter(correo=email, estado="A")
        serializer = PersonaSerializer(persona, many=True)
        return Response(serializer.data)


class AlumnoViewsets(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    def listar(self, request):
        queryset = Alumno.objects.all()
        serializer = AlumnoSerializer(queryset, many=True)
        return Response(serializer.data)


class MatriculaViewsets(viewsets.ViewSet):

    def listar_Matricula_id(self, request, id):
        usuario = User.objects.get(id=id)
        queryset = Matricula.objects.filter(
            alumno__persona__numeroDocumento=usuario.dni)
        serializer = MatriculaSerializer(queryset, many=True)
        return Response(serializer.data)

    def listar_Detalle_Matricula_id(self, request, id):
        matricula = Matricula.objects.get(id=id)
        queryset = DetalleMatricula.objects.filter(
            matricula=matricula, estado="A")
        serializer = DetalleMatriculaSerializer(queryset, many=True)
        return Response(serializer.data)


class CalificacionesViewsets(viewsets.ViewSet):

    def listar_todas_Calificaciones_idPersona(self, request, dni):
        usuario = User.objects.get(dni=dni)              
        queryset = DetalleMatricula.objects.filter(
            matricula__alumno__persona__numeroDocumento=usuario.dni, estado="A")
        serializer = DetalleMatriculaSerializer(queryset, many=True)
        return Response(serializer.data)
    # -----------------------
    def listar_Calificaciones_idPersona(self, request, id):
        usuario = User.objects.get(id=id)
        queryset = Matricula.objects.filter(
            alumno__persona__numeroDocumento=usuario.dni)
        serializer = MatriculaSerializer(queryset, many=True)
        return Response(serializer.data)

    def listar_CalificacionesDetall_idMatri(self, request, id):
        matricula = Matricula.objects.get(id=id)
        queryset = DetalleMatricula.objects.filter(
            matricula=matricula, estado="A")
        serializer = DetalleMatriculaSerializer(queryset, many=True)
        return Response(serializer.data)


class ReporteEconomicoViewsets(viewsets.ViewSet):

    def listar_ReporteEconomico_id(self, request, id):
        usuario = User.objects.get(id=id)
        reportEco = ReporteEconomico.objects.get(
            alumno__persona__numeroDocumento=usuario.dni)
        queryset = ReporteEcoConceptoPago.objects.filter(
            reporteEconomico=reportEco, estado="A")
        serializer = ReporteEcoConceptoPagoSerializer(
            queryset, many=True)
        return Response(serializer.data)
