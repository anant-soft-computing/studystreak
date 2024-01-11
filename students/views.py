from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework import generics

# Create your views here.

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
