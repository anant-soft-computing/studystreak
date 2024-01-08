from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from rest_framework.filters import SearchFilter
from .serializers import (
    CourseCreateSerializers,
    CourseListSerializers,
    CourseRetUpdDelSerializers,
   
)

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializers

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['Category__name', 'Level__name']
    search_fields = ['Course_Title', ]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CourseCreateSerializers
        return super().get_serializer_class()

class CourseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetUpdDelSerializers


