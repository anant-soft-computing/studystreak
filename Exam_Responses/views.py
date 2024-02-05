from django.shortcuts import render
from .serializers import StudentAnswerSerializers
from rest_framework import generics
from .models import StudentAnswer

class StudentAnswerListView(generics.ListCreateAPIView):
    # queryset = StudentAnswer
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializers
