from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

# Create your views here.
from .models import Answer, Exam, FullLengthTest
from .serializers import AnswerSerializer, ExamSerializer, FullLengthTestSerializer
# from Studentanswer.models import Studentanswer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def create(self, request, *args, **kwargs):
        # answer_data = request.data.pop("answers")

        return super().create(request, *args, **kwargs)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class FullLengthTestViewSet(viewsets.ModelViewSet):
    queryset = FullLengthTest.objects.all()
    serializer_class = FullLengthTestSerializer

# def create_student_answer(student, exam, question_number, answer_text):
#     studentanswer_obj = Studentanswer.create(student=student,exam=exam, question_number=question_number, answer_text=answer_text)
#     studentanswer_obj.save()
