from rest_framework import serializers
from exam.models import Studentanswer

class StudentanswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studentanswer
        fields = ['id', 'student', 'exam', 'question_number', 'answer_text']
        