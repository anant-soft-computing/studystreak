from django.db import models
from froala_editor.fields import FroalaField

from master.models import ExamType, QuestionType


# Create your models here.
class Exam(models.Model):
    exam_Name = models.CharField(max_length=10)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    passage = FroalaField()
    no_of_questions = models.IntegerField(default=4)
    question = FroalaField()

    def __str__(self):
        return self.exam_Name

    class Meta:
        verbose_name = "Exam_Block"


class Answer(models.Model):
    exam = models.ForeignKey(Exam, related_name="answers", on_delete=models.CASCADE)
    question_number = (
        models.IntegerField()
    )  # Indicates which question this answer corresponds to
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text

    class Meta:
        unique_together = ("exam", "question_number")
