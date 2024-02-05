from rest_framework import serializers
from .models import StudentAnswer, Student_Answer

class StudentAnswerAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student_Answer
        fields = ("question_number", "answer_text")


class StudentAnswerSerializers(serializers.ModelSerializer):
    student_answers = serializers.SerializerMethodField()
    class Meta:
        model = StudentAnswer
        fields = "__all__"
        depth=2

    def get_student_answers(self, obj):
        student_answers = Student_Answer.objects.filter(student_exam=obj)
        return StudentAnswerAnswerSerializers(student_answers, many=True).data