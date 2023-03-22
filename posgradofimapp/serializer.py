from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime
# from django.contrib.auth.models import User
from posgradofimapp.models import Persona
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'dni')


class PersonaLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('numeroDocumento', 'primerNombre',
                  'apellidoPaterno', 'apellidoMaterno', 'correo')


class CustomObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["primerNombre"] = user.primerNombre
        token["segundoNombre"] = user.segundoNombre
        token["apellidoPaterno"] = user.apellidoPaterno
        token["apellidoMaterno"] = user.apellidoMaterno

        return token


class calificativoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)
    estado = serializers.CharField(max_length=1)


class conceptoPagoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)
    estado = serializers.CharField(max_length=1)


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tipoDocumento = serializers.CharField(max_length=50)
    numeroDocumento = serializers.CharField(max_length=50)
    primerNombre = serializers.CharField(max_length=100)
    segundoNombre = serializers.CharField(max_length=100)
    apellidoPaterno = serializers.CharField(max_length=100)
    apellidoMaterno = serializers.CharField(max_length=100)
    correo = serializers.CharField(max_length=100)
    estado = serializers.CharField(max_length=1)


class MaestriaSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=10)
    nombre = serializers.CharField(max_length=100)
    estado = serializers.CharField(max_length=1)


class CursoSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=10)
    nombre = serializers.CharField(max_length=100)
    credito = serializers.IntegerField()
    estado = serializers.CharField(max_length=1)


class PeriodoSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=10)
    nombre = serializers.CharField(max_length=100)
    estado = serializers.CharField(max_length=1)


class AlumnoSerializer(serializers.Serializer):
    persona = PersonaSerializer()
    maestria = MaestriaSerializer()
    periodoDeIngreso = PeriodoSerializer()
    codigoUniPreGrado = serializers.CharField(max_length=10)
    estadoAcademico = serializers.CharField(max_length=1)
    estado = serializers.CharField(max_length=1)


class DocenteSerializer(serializers.Serializer):
    persona = PersonaSerializer()
    maestria = MaestriaSerializer()
    estado = serializers.CharField(max_length=1)


class SeccionSerializer(serializers.Serializer):
    maestria = MaestriaSerializer()
    periodo = PeriodoSerializer()
    curso = CursoSerializer()
    docente = DocenteSerializer()
    aulaWeb = serializers.CharField(max_length=100)
    estado = serializers.CharField(max_length=1)


class GraduadoSerializer(serializers.Serializer):
    alumno = AlumnoSerializer()
    tituloTesis = serializers.CharField(max_length=300)
    fechaGraduado = serializers.CharField(max_length=50)
    asesor = serializers.CharField(max_length=200)
    primerEspecialista = DocenteSerializer()
    segundoEspecialista = DocenteSerializer()
    promedio = serializers.FloatField()
    calificativo = serializers.CharField(max_length=50)
    estado = serializers.CharField(max_length=1)


class MatriculaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    alumno = AlumnoSerializer()
    periodo = PeriodoSerializer()
    estado = serializers.CharField(max_length=1)
    fechaRegistro = serializers.CharField(max_length=50)


class DetalleMatriculaSerializer(serializers.Serializer):
    matricula = MatriculaSerializer()
    seccion = SeccionSerializer()
    promedioTrabajos = serializers.FloatField()
    examenParcial = serializers.FloatField()
    examenFinal = serializers.FloatField()
    promedioFinal = serializers.FloatField()
    retirado = serializers.FloatField()
    estado = serializers.CharField(max_length=1)


class EstadoBoletaPagoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)
    estado = serializers.CharField(max_length=1)


class ReporteEconomicoSerializer(serializers.Serializer):
    alumno = AlumnoSerializer()
    estado = serializers.CharField(max_length=1)


class ReporteEcoConceptoPagoSerializer(serializers.Serializer):
    reporteEconomico = ReporteEconomicoSerializer()
    conceptoPago = conceptoPagoSerializer()
    periodo = PeriodoSerializer()
    monto = serializers.FloatField()
    numeroRecibo = serializers.CharField(max_length=100)
    estadoBoletaPago = EstadoBoletaPagoSerializer()
    estado = serializers.CharField(max_length=1)
