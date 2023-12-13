from django.shortcuts import render
from .serializers import LessonListSerializers
from .models import Lesson
from rest_framework import generics

# Create your views here.

class LessonListView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializers


class LessionRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializers
    

