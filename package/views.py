from django.shortcuts import render
from .models import Package
from .serializers import PackageListSerializers, PackageRetUpdDelSerializers, CoursePackageSerializer, CourseListsSerializers
from rest_framework import generics
from Courses.models import Course
# Create your views here.

class PackageListView(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageListSerializers
    
    
class PackageRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageRetUpdDelSerializers
    
    
class CoursePackageView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePackageSerializer
   

class ListofCourse(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = CourseListsSerializers