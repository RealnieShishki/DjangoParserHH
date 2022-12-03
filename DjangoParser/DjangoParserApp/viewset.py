from django.urls import path, include
from django.contrib.auth.models import User
from .Serializer import UserSerializer
from rest_framework import routers, serializers, viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


