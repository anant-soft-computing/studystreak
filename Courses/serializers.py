from rest_framework import serializers
from .models import Course



class CourseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
        depth = 2
        

class CourseRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
        depth = 2