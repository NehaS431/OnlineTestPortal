from django.shortcuts import render
from django.http import JsonResponse
# from backend.backend import api
# from backend.backend.api import serializer 
from rest_framework.decorators import  api_view
from rest_framework.response import Response 
from api.serializer import MyTokenObtainPairSerializer,RegisterSerializer
from rest_framework_simplejwt.views import  TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User


# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class=RegisterSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)

