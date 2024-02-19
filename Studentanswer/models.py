from django.db import models
from django.contrib.auth.models import User
# from exam.models import Exam

# class Studentanswer(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     # exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='student_answers')
#     exam = models.IntegerField()
#     question_number = models.IntegerField()
#     answer_text = models.TextField()

#     def __str__(self):
#         return f"{self.student.username} - Q{self.question_number}: {self.answer_text}"
