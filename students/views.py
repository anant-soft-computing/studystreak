from django.shortcuts import render
from .serializers import StudentSerializers, StudentRetUpdDelSerializers
from .models import Student
from rest_framework import generics

# Create your views here.

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user=user)

class StudentRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRetUpdDelSerializers

    
    
