from .serializers import *
from rest_framework import generics
from .models import Student_answer

class StudentAnswerListView(generics.ListCreateAPIView):
    queryset = Studentanswer.objects.all()
    serializer_class = StudentAnswerSerializers


