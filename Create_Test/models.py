from django.db import models

# Create your models here.
from exam.models import Exam, ExamType

class module(models.Model):
    Name = models.CharField(max_length = 100, null=True, blank=True)
    Reading = models.ManyToManyField(Exam, null=True, blank=True, related_name="reading+")
    Listening = models.ManyToManyField(Exam, null=True, blank=True, related_name="listening+")
    Speaking = models.ManyToManyField(Exam, null=True, blank=True, related_name="Speaking+")
    Writing = models.ManyToManyField(Exam, null=True, blank=True, related_name="writing+")
    
    def __str__(self):
         return f"{self.Reading} - {self.Listening} - {self.Speaking} - {self.Writing}"

class createexam(models.Model):
   
    IELTS = models.ForeignKey('module',on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.IELTS)