from django.shortcuts import render
from .models import Course
from .serializers import CourseListSerializers, CourseRetUpdDelSerializers
from rest_framework import generics


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializers


class CourseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetUpdDelSerializers
