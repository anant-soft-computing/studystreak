from django.shortcuts import render
from rest_framework import generics
from .models import createexam
from rest_framework import status
from .serializers import createexamserializers


# Create your views here.


class createexamview(generics.ListCreateAPIView):
    queryset = createexam.objects.all()
    serializer_class = createexamserializers