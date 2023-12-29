from rest_framework import generics

from .models import Course
from .serializers import (
    CourseCreateSerializers,
    CourseListSerializers,
    CourseRetUpdDelSerializers,
)


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializers

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CourseCreateSerializers
        return super().get_serializer_class()


class CourseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetUpdDelSerializers
