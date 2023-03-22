from django.shortcuts import render
from django.http import HttpResponse
from posgradofimapp.models import Colaborador, Persona
from posgradofimapp.serializer import CustomObtainPairSerializer, CustomTokenObtainPairSerializer, UserSerializer, PersonaLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.backends import TokenBackend

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
# Create your views here.


class Login_jwt(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
       
        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Exitoso',
                    'ok': True,
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filer(id=request.data.get('user', ''))
        if user.exist():
            RefreshToken.for_user(user.first())
            return response({'menssage': 'Sesiòn cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe ese usuario'}, status=status.HTTP_400_BAD_REQUEST)


# class LoginAPI(APIView):
#     def post(self, request):
#         login_data = request.data
#         email = login_data["correo"]
#         password = login_data.get("password")
#         user = Persona.objects.filter(
#             correo=email, numeroDocumento=password, estado="A").first()
#         if user != None:
#             token = CustomObtainPairSerializer.get_token(user)

#             return Response({
#                 'ok': True,
#                 'token': str(token),
#                 'id': str(user.id),
#             })

#         return HttpResponse("ok")


class VerificarAPI(APIView):
    def post(self, request):
        tokencino = request.data
        llave = tokencino["token"]
        try:
            valid_data = TokenBackend(
                algorithm='HS256').decode(llave, verify=False)

            if valid_data != None:
                return Response({
                    'ok': True,
                    'content': "Token valido",
                })

            return HttpResponse("ok")
        except Exception as e:
            return Response({
                'ok': False,
                'content': "No esta autenticado para realizar la solicitud",
            })
            return HttpResponse("ok")


# class LoginColaborador(APIView):
#     def post(self, request):
#         login_data = request.data
#         email = login_data["correo"]
#         password = login_data.get("password")
#         colaborador = Colaborador.objects.filter(
#             persona__correo__exact=email, password=password, estado='A').first()

#         if colaborador != None:
#             token = CustomObtainPairSerializer.get_token(colaborador.persona)

#             return Response({
#                 'ok': True,
#                 'token': str(token),
#                 'id': str(colaborador.id),
#             })

#         return HttpResponse("ok")
