from rest_framework import serializers

from .models import Answer, Exam


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer()

    class Meta:
        model = Exam
        fields = "__all__"
