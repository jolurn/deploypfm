from posgradofimapp.models import Colaborador, Graduado, Calificativo, EstadoAcademico, EstadoBoletaP, TipoDocumento, DetalleMatricula, Docente, ConceptoPago, Seccion, Maestria, Curso, Periodo, Persona, Alumno, Matricula, ReporteEconomico, ReporteEcoConceptoPago, User, TipoUsuario
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    search_fields = ['dni', 'last_name','username']
    ordering = ['last_name']
    list_display = ('username', 'first_name', 'last_name',
                    'email', 'usu_tipo', 'dni', 'password')

    def save_model(self, request, obj, form, change):
        if obj.password.startswith('pbkdf2'):
            obj.password = obj.password
        else:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)


class TipoUsuarioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('nombre', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(TipoUsuario, TipoUsuarioAdmin)


class EstadoBoletaPAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('nombre', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(EstadoBoletaP, EstadoBoletaPAdmin)


class ConceptoPagoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('nombre', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(ConceptoPago, ConceptoPagoAdmin)


class EstadoAcademicoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('nombre', 'estado', 'fechaRegistro', 'usuarioPosgradoFIM')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(EstadoAcademico, EstadoAcademicoAdmin)


class CalificativoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('nombre', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Calificativo, CalificativoAdmin)


class TipoDocumentoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    ordering = ['nombre']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('nombre', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(TipoDocumento, TipoDocumentoAdmin)


class MaestriaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    ordering = ['codigo']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('codigo', 'nombre', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Maestria, MaestriaAdmin)


class CursoAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    ordering = ['codigo']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('codigo', 'nombre', 'credito', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Curso, CursoAdmin)


class PeriodoAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    ordering = ['codigo']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('codigo', 'nombre', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Periodo, PeriodoAdmin)


class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['apellidoPaterno', 'correo', 'numeroDocumento']
    ordering = ['apellidoPaterno']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('tipoDocumento', 'numeroDocumento', 'primerNombre', 'segundoNombre',
                    'apellidoPaterno', 'apellidoMaterno', 'correo', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Persona, PersonaAdmin)


class AlumnoAdmin(admin.ModelAdmin):
    search_fields = ['persona__apellidoPaterno', 'persona__numeroDocumento']
    autocomplete_fields = ['persona', 'periodoDeIngreso']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('persona', 'maestria', 'periodoDeIngreso',
                    'codigoUniPreGrado', 'estadoAcademico', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Alumno, AlumnoAdmin)


class ColaboradorAdmin(admin.ModelAdmin):
    search_fields = ['persona__apellidoPaterno']
    autocomplete_fields = ['persona']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('persona', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Colaborador, ColaboradorAdmin)


class DocenteAdmin(admin.ModelAdmin):
    search_fields = ['persona__apellidoPaterno']
    autocomplete_fields = ['persona']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('persona', 'maestria', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Docente, DocenteAdmin)


class SeccionAdmin(admin.ModelAdmin):
    # Para que sea mas facil de encontrar a la hora de crear una matricula
    search_fields = ['periodo__codigo', 'maestria__codigo', 'curso__codigo']
    autocomplete_fields = ['curso', 'periodo', 'docente', 'maestria']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('curso', 'docente', 'periodo', 'maestria',
                    'aulaWeb', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Seccion, SeccionAdmin)


class GraduadoAdmin(admin.ModelAdmin):
    search_fields = ['alumno__persona__apellidoPaterno',
                     'alumno__persona__numeroDocumento']
    autocomplete_fields = ['alumno', 'calificativo',
                           'primerEspecialista', 'segundoEspecialista']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('alumno', 'tituloTesis', 'fechaGraduado', 'asesor', 'primerEspecialista',
                    'segundoEspecialista', 'promedio', 'calificativo', 'estado', 'fechaRegistro')

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Graduado, GraduadoAdmin)


class DetalleMatriculaAdmin(admin.TabularInline):
    model = DetalleMatricula
    extra = 0
    autocomplete_fields = ['seccion']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


class MatriculaAdmin(admin.ModelAdmin):
    search_fields = ['alumno__persona__apellidoPaterno',
                     'alumno__persona__numeroDocumento', 'periodo__codigo']
    autocomplete_fields = ['alumno', 'periodo']
    inlines = [DetalleMatriculaAdmin, ]
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('alumno', 'periodo', 'estado', 'fechaRegistro')
    filter_horizontal = ['seccion']

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(Matricula, MatriculaAdmin)

# class CalificacionAdmin(admin.ModelAdmin):
#   list_display = ('detalleMatricula','nota','estado','fechaRegistro')

# admin.site.register(Calificacion,CalificacionAdmin)


class ReporteEcoConceptoPagoAdmin(admin.TabularInline):
    model = ReporteEcoConceptoPago
    extra = 0
    autocomplete_fields = ['conceptoPago', 'periodo']
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


class ReporteEconomicoAdmin(admin.ModelAdmin):
    search_fields = ['alumno__persona__apellidoPaterno',
                     'alumno__persona__numeroDocumento']
    autocomplete_fields = ['alumno']
    inlines = [ReporteEcoConceptoPagoAdmin, ]
    # --- poner en solo lectura los input ---
    exclude = ('fechaRegistro', 'fechaModificado',
               'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
    readonly_fields = ('fechaRegistro', 'fechaModificado',
                       'fechaElimnado', 'usuarioPosgradoFIM', 'ipUsuario')
# ----- Fin poner en solo lectura los input -----
    list_display = ('alumno', 'estado', 'fechaRegistro')
    filter_horizontal = ['conceptoPago']

    def save_model(self, request, obj, form, change):
        # request.user es el usuario autenticado en ese momento

        obj.usuarioPosgradoFIM = request.user.first_name+' '+request.user.last_name
        super().save_model(request, obj, form, change)


admin.site.register(ReporteEconomico, ReporteEconomicoAdmin)
