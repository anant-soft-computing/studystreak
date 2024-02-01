from rest_framework import serializers
from .models import StudentAnswer



class StudentAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = "__all__"