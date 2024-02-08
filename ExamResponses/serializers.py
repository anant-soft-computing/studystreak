from rest_framework import serializers
from .models import Studentanswer, Student_answer

class StudentAnswerAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_answer
        fields = ("question_number", "answer_text")

class StudentAnswerSerializers(serializers.ModelSerializer):
    student_answers = serializers.SerializerMethodField()

    class Meta:
        model = Studentanswer
        fields = ("id", "user", "exam", "student_answers")

    def get_student_answers(self, obj):
        student_answers = Student_answer.objects.filter(student_exam=obj)
        serialized_answers = StudentAnswerAnswerSerializers(student_answers, many=True).data
        return serialized_answers