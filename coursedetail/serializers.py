from rest_framework import serializers
from .models import  Lesson, QuizOption, Quiz_Question
from rest_framework import generics

class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
    
    
class LessionRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = Lesson
        fields = '__all__'


class QuizOptionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = '__all__'

    
class Quiz_QuestionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz_Question
        fields = '__all__'