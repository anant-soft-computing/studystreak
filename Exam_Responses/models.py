from django.db import models
from django.contrib.auth.models import User
from exam.models import Exam

# Create your models here.


# class StudentAnswer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     exam = models.ForeignKey(Exam, related_name="exam", on_delete=models.CASCADE, null=False)
    # question_number = (
    #     models.IntegerField()
    # )  
    # answer_text = models.TextField()

    # def __str__(self):
    #     return self.answer_text
    
    # class Meta:
    #     unique_together = ("exam", "question_number", "user")
# class Student_Answer(models.Model):
#     student_exam = models.ForeignKey(StudentAnswer, related_name="student_exam", on_delete=models.CASCADE)
#     question_number = (
#         models.IntegerField()
#     ) 
#     answer_text = models.TextField()

#     def __str__(self):
#         return self.answer_text


class Studentanswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    exam = models.ForeignKey(Exam, related_name="exam", on_delete=models.CASCADE, null=False)

class Student_answer(models.Model):
    student_exam = models.ForeignKey(Studentanswer, related_name="student_exam", on_delete=models.CASCADE)
    question_number = (
        models.IntegerField()
    ) 
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text