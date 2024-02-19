from rest_framework import generics
from exam.models import Studentanswer
from .serializer import StudentanswerSerializer


class StudentAnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSerializer

class StudentAnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Studentanswer.objects.all()
    serializer_class = StudentanswerSerializer
