from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from .models import LiveClass
from .serializers import LiveClassListSerializer

# Create your views here.

class LiveClassListView(generics.ListCreateAPIView):
    queryset = LiveClass.objects.all()
    serializer_class = LiveClassListSerializer
    
class LiveClassRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LiveClass.objects.all()
    serializer_class = LiveClassListSerializer