from django.shortcuts import render
from .serializers import StudentAnswerSerializers
from rest_framework import generics
from .models import Studentanswer

class StudentAnswerListView(generics.ListCreateAPIView):
    # queryset = StudentAnswer
    queryset = Studentanswer.objects.all()
    serializer_class = StudentAnswerSerializers
