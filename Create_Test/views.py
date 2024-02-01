from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import createexam, Responses
from rest_framework import status
from .serializers import createexamserializers, ResponsesSerializers


# Create your views here.


class createexamview(generics.ListCreateAPIView):
    queryset = createexam.objects.all()
    serializer_class = createexamserializers


class ResponsesView(generics.ListCreateAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializers