from ckeditor.fields import RichTextField
from django.db import models

from master.models import ExamType, QuestionType


class BlockType(models.TextChoices):
    practice = "Practice", "Practice"
    full_length = "Full Length", "Full Length"
    both = "Both", "Both"


class Difficulty(models.TextChoices):
    easy = "Easy", "Easy"
    medium = "Medium", "Medium"
    hard = "Hard", "Hard"


# Create your models here.
class Exam(models.Model):
    exam_name = models.CharField(max_length=10)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    passage = RichTextField()
    no_of_questions = models.IntegerField(default=4)
    question = RichTextField()
    block_type = models.CharField(max_length=20, choices=BlockType.choices, null=True)
    difficulty_level = models.CharField(
        max_length=20, choices=Difficulty.choices, null=True
    )
    block_threshold = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.exam_name

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
