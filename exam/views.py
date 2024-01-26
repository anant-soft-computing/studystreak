from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

# Create your views here.
from .models import Answer, Exam, FullLengthTest
from .serializers import AnswerSerializer, ExamSerializer, FullLengthTestSerializer, ExamListSerializers
from rest_framework import generics 

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


class ExamListView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class =  ExamListSerializers


class ExamListFilterView(generics.ListAPIView):
    serializer_class = ExamListSerializers

    def get_queryset(self):
        block_type = self.request.query_params.get('block_type', None)
        queryset = Exam.objects.all()

        if block_type:
            queryset = queryset.filter(block_type=block_type)

        return queryset
