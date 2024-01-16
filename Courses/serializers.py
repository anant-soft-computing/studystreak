from rest_framework import serializers

from .models import Course
from master.serializers import AdditionalResourceListSerializers, CourseMaterialListSerializers
from coursedetail.serializers import LessonListSerializers

class CourseListSerializers(serializers.ModelSerializer):
    lessons = LessonListSerializers(many=True, read_only=True)
    course_materials = CourseMaterialListSerializers(many=True, read_only=True)
    additional_resources = AdditionalResourceListSerializers(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

        depth = 2


class CourseCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

        depth = 2


