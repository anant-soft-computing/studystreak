from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class module(models.Model):
    
    Reading = models.ManyToManyField("QuestionBank.ReadingQuestion")
    Listening = models.ManyToManyField("QuestionBank.Listening_Question")
    Speaking = models.ManyToManyField("QuestionBank.SpeakingQuestion")
    Writing = models.ManyToManyField("QuestionBank.WritingQuestion")
    
    def __str__(self):
         return f"{self.Reading} - {self.Listening} - {self.Speaking} - {self.Writing}"

class createexam(models.Model):
   
    IELTS = models.ForeignKey('module',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.IELTS)