from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from rest_framework.filters import SearchFilter
from .serializers import (
    CourseCreateSerializers,
    CourseListSerializers,
    CourseRetUpdDelSerializers,
   
)
from master.models import CourseMaterial, AdditionalResource
from master.serializers import CourseMaterialListSerializers, AdditionalResourceListSerializers
from rest_framework.response import Response

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

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data

        for course_data in data:
            course_id = course_data['id']
            course_materials = CourseMaterial.objects.filter(course_id=course_id)
            additional_resources = AdditionalResource.objects.filter(course_id=course_id)

            course_materials_serializer = CourseMaterialListSerializers(course_materials, many=True, read_only=True)
            additional_resources_serializer = AdditionalResourceListSerializers(additional_resources, many=True, read_only=True)

            course_data['course_materials'] = course_materials_serializer.data
            course_data['additional_resources'] = additional_resources_serializer.data

        return Response(data)

class CourseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetUpdDelSerializers


