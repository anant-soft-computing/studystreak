from rest_framework import serializers
from .models import  Lesson
from rest_framework import generics

class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
    
    
class LessionRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Lesson
        fields = '__all__'