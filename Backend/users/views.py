from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import CustomUser
from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
