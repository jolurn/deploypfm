# from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))


Es1 = 'A'
Es2 = 'I'
ESTADO_OFERTA = [
    (Es1, 'Activo'),
    (Es2, 'Inactivo')
]


class TipoUsuario(models.Model):

    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name_plural = "Tipo de Usuarios"


class UsuarioManager(BaseUserManager):

    def create_user(self, email, username, first_name, last_name, dni, password=None):
        if not dni:
            raise ValueError('El usuario debe tener un DNI')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dni=dni
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, username, first_name, last_name, dni, password):
        user = self.create_user(
            email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            dni=dni
        )

        user.save(using=self._db)
        return user


class User(AbstractUser):

    dni = models.CharField(max_length=100)
    usu_tipo = models.ForeignKey(
        TipoUsuario, null=True, on_delete=models.SET_NULL)

    objects = UsuarioManager()

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'dni']

    def nombre_completo(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name_plural = "Usuarios"


class EstadoAcademico(models.Model):

    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name_plural = "Estados Academico"


class TipoDocumento(models.Model):

    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name_plural = "Tipo de Documentos"


class EstadoBoletaP(models.Model):

    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Estados Boletas Pagos"


class ConceptoPago(models.Model):

    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Conceptos de Pagos"


class Maestria(models.Model):

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return "{} - {}".format(self.codigo, self.nombre)

    class Meta:
        verbose_name_plural = "Maestrias"


class Curso(models.Model):

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    credito = models.IntegerField()
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return "{} - {}".format(self.codigo, self.nombre)

    class Meta:
        verbose_name_plural = "Cursos"


class Periodo(models.Model):

    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Periodos"


class Persona(models.Model):

    tipoDocumento = models.ForeignKey(
        TipoDocumento, null=True, on_delete=models.SET_NULL)
    numeroDocumento = models.CharField(max_length=100)
    primerNombre = models.CharField(max_length=100)
    segundoNombre = models.CharField(max_length=100, null=True, blank=True)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def nombre_completos(self):
        return "{} {}, {} {}".format(self.apellidoPaterno, self.apellidoMaterno, self.primerNombre, self.segundoNombre)

    def __str__(self):
        return self.nombre_completos()

    class Meta:
        verbose_name_plural = "Personas"


class Alumno(models.Model):

    persona = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)
    maestria = models.ForeignKey(
        Maestria, null=True, on_delete=models.SET_NULL)
    periodoDeIngreso = models.ForeignKey(
        Periodo, null=True, blank=True, on_delete=models.SET_NULL)
    codigoUniPreGrado = models.CharField(max_length=10, null=True, blank=True)
    estadoAcademico = models.ForeignKey(
        EstadoAcademico, null=True, on_delete=models.SET_NULL)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def nombre_completo(self):
        return "{} {} {} {}, {}".format(self.persona.apellidoPaterno, self.persona.apellidoMaterno, self.persona.primerNombre, self.persona.segundoNombre, self.maestria.codigo)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name_plural = "Alumnos"


class Colaborador(models.Model):

    persona = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)
    password = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def nombre_completo(self):
        return "{} {}, {} {}".format(self.persona.apellidoPaterno, self.persona.apellidoMaterno, self.persona.primerNombre, self.persona.segundoNombre)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name_plural = "Colaboradores"


class Docente(models.Model):

    persona = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)
    maestria = models.ForeignKey(
        Maestria, null=True, on_delete=models.SET_NULL)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def nombre_completo(self):
        return "{} {}, {} {}".format(self.persona.apellidoPaterno, self.persona.apellidoMaterno, self.persona.primerNombre, self.persona.segundoNombre)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name_plural = "Docentes"


class Seccion(models.Model):

    maestria = models.ForeignKey(
        Maestria, null=True, on_delete=models.SET_NULL)
    periodo = models.ForeignKey(Periodo, null=True, on_delete=models.SET_NULL)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)
    docente = models.ForeignKey(Docente, null=True, on_delete=models.SET_NULL)
    aulaWeb = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def nombre_completo(self):
        return "{} - {} {} - {} {} {}".format(self.periodo.codigo, self.maestria.codigo, self.curso.codigo, self.curso.nombre, self.docente.persona.apellidoPaterno, self.docente.persona.apellidoMaterno, self.docente.persona.primerNombre)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name_plural = "Secciones"


class Matricula(models.Model):

    alumno = models.ForeignKey(Alumno, null=True, on_delete=models.SET_NULL)
    seccion = models.ManyToManyField(
        Seccion, through='DetalleMatricula', blank=True,)
    periodo = models.ForeignKey(Periodo, null=True, on_delete=models.SET_NULL)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def nombre_completo(self):
        return "{} {}, {} {}".format(self.alumno.persona.apellidoPaterno, self.alumno.persona.apellidoMaterno, self.alumno.persona.primerNombre, self.alumno.persona.segundoNombre)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name_plural = "Matriculas"


class DetalleMatricula(models.Model):

    matricula = models.ForeignKey(
        Matricula, null=True, on_delete=models.SET_NULL)
    seccion = models.ForeignKey(Seccion, null=True, on_delete=models.SET_NULL)
    promedioTrabajos = models.FloatField(null=True, blank=True)
    examenParcial = models.FloatField(null=True, blank=True)
    examenFinal = models.FloatField(null=True, blank=True)
    promedioFinal = models.FloatField(null=True, blank=True)
    retirado = models.BooleanField(default=False)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return "{}  {}, {} {}".format(self.matricula.alumno.persona.apellidoPaterno, self.matricula.alumno.persona.apellidoMaterno, self.seccion.curso, self.seccion.periodo)

    class Meta:
        verbose_name_plural = "Detalle de Matriculas"


class Calificativo(models.Model):

    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Calificativos"


class Graduado(models.Model):

    alumno = models.ForeignKey(Alumno, null=True, on_delete=models.SET_NULL)
    tituloTesis = models.CharField(max_length=300)
    fechaGraduado = models.DateField(null=True, blank=True)
    asesor = models.CharField(max_length=200)
    primerEspecialista = models.ForeignKey(
        Docente, related_name='primerEspecialista_article_set', null=True, on_delete=models.SET_NULL)
    segundoEspecialista = models.ForeignKey(
        Docente, related_name='segundoEspecialista_article_set', null=True, on_delete=models.SET_NULL)
    promedio = models.FloatField(null=True, blank=True)
    calificativo = models.ForeignKey(
        Calificativo, null=True, on_delete=models.SET_NULL)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    def __str__(self):
        return "{}  {}, {} {} {}".format(self.alumno.persona.apellidoPaterno, self.alumno.persona.apellidoMaterno, self.tituloTesis, self.fechaGraduado, self.asesor)

    class Meta:
        verbose_name_plural = "Graduados"


class ReporteEconomico(models.Model):

    alumno = models.ForeignKey(Alumno, null=True, on_delete=models.SET_NULL)
    conceptoPago = models.ManyToManyField(
        ConceptoPago, through='ReporteEcoConceptoPago', blank=True,)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)

    class Meta:

        verbose_name_plural = "Reportes Economicos"


class ReporteEcoConceptoPago(models.Model):

    reporteEconomico = models.ForeignKey(
        ReporteEconomico, null=True, on_delete=models.SET_NULL)
    conceptoPago = models.ForeignKey(
        ConceptoPago, null=True, on_delete=models.SET_NULL)
    periodo = models.ForeignKey(Periodo, null=True, on_delete=models.SET_NULL)
    monto = models.FloatField()
    numeroRecibo = models.CharField(max_length=100, null=True, blank=True)
    estadoBoletaPago = models.ForeignKey(
        EstadoBoletaP, null=True, on_delete=models.SET_NULL)
    estado = models.CharField(max_length=1, choices=ESTADO_OFERTA, default='A')
    fechaRegistro = models.DateField(default=datetime.now())
    fechaModificado = models.DateField(null=True, blank=True, auto_now=True)
    fechaElimnado = models.DateField(null=True, blank=True)
    ipUsuario = models.CharField(null=True, default=s.getsockname()[
                                 0], blank=True, max_length=100)
    usuarioPosgradoFIM = models.CharField(
        null=True, blank=True, max_length=200)
