"""intposgradof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posgradofimapp.viewsets import MatriculaViewsets, PersonaViewsets, CalificacionesViewsets, ReporteEconomicoViewsets, AlumnoViewsets
from posgradofimapp.views import VerificarAPI, Login_jwt
# from posgradofimapp.views import VerificarAPI

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login', LoginAPI.as_view()),
    # path('loginColaborador', LoginColaborador.as_view()),

    path('loginjwt', Login_jwt.as_view()),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('matriculacurso/<per>/<ma>/<cu>', MatriculaViewsets.as_view({'put':'listar_Por_Curso'})),
    # path('matricula', MatriculaViewsets.as_view({'get':'listar'})),
    # path('matriculaDetalle', MatriculaViewsets.as_view({'get':'listar_DetalleMat'})),
    path('persona', PersonaViewsets.as_view({'get': 'listar'})),

    path('wachiman', VerificarAPI.as_view()),
    path('alumno', AlumnoViewsets.as_view({'get': 'listar'})),
    path('persona/<email>',
         PersonaViewsets.as_view({'put': 'listar_persona_email'})),
    path('matri/<dni>',
         CalificacionesViewsets.as_view({'put': 'listar_todas_Calificaciones_idPersona'})),
    path('matricula/<id>',
         MatriculaViewsets.as_view({'put': 'listar_Matricula_id'})),
    path('matriculaDetalle/<id>',
         MatriculaViewsets.as_view({'put': 'listar_Detalle_Matricula_id'})),
    path('calificaciones/<id>',
         CalificacionesViewsets.as_view({'put': 'listar_Calificaciones_idPersona'})),
    path('calificacionesDetalle/<id>',
         CalificacionesViewsets.as_view({'put': 'listar_CalificacionesDetall_idMatri'})),
    path('reporteeconomico/<id>',
         ReporteEconomicoViewsets.as_view({'put': 'listar_ReporteEconomico_id'})),

]
