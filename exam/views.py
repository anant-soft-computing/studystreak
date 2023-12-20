from rest_framework import viewsets

# Create your views here.
from .models import Answer, Exam
from .serializers import AnswerSerializer, ExamSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
