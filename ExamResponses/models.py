from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from exam.models import Exam


class Studentanswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)


class Student_answer(models.Model):
    student_exam = models.ForeignKey(Studentanswer, on_delete=models.CASCADE)
    question_number = models.IntegerField()
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
