from django.shortcuts import render
from .models import Package
from .serializers import PackageListSerializers, PackageRetUpdDelSerializers
from rest_framework import generics

# Create your views here.

class PackageListView(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageListSerializers
    
    
class PackageRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageRetUpdDelSerializers
    
    
