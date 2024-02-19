from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from master.models import ExamType, TestType
from django.contrib.auth.models import User
# from .views import create_student_answer
# from Studentanswer.models import Studentanswer


class BlockType(models.TextChoices):
    practice = "Practice", "Practice"
    full_length = "Full Length", "Full Length"
    both = "Both", "Both"


class Difficulty(models.TextChoices):
    easy = "Easy", "Easy"
    medium = "Medium", "Medium"
    hard = "Hard", "Hard"


class ExamType(models.TextChoices):
    reading = "Reading", "Reading"
    listening = "Listening", "Listening"
    speaking = "Speaking", "Speaking"
    writing = "Writing", "Writing"


# Create your models here.
class Exam(models.Model):
    exam_name = models.CharField(max_length=10)
    exam_type = models.CharField(
        max_length=20,
        choices=ExamType.choices,
        default=ExamType.reading,
        help_text="(Reading, Listening, Speaking, Writing)",
    )
    test_type = models.ForeignKey(TestType, on_delete=models.SET_NULL, null=True)
    # question_type = models.ManyToManyField(QuestionType, null=True)
    passage = RichTextUploadingField("contents", null=True, blank=True)
    no_of_questions = models.IntegerField(default=4)
    question = RichTextField()
    block_type = models.CharField(max_length=20, choices=BlockType.choices, null=True)
    difficulty_level = models.CharField(
        max_length=20, choices=Difficulty.choices, null=True
    )
    block_threshold = models.PositiveIntegerField(null=True)
    type_of_module = models.ForeignKey(
        "master.ModuleType", on_delete=models.SET_NULL, null=True
    )
    audio_file = models.FileField(upload_to="examblockaudio/", null=True, blank=True)

    def __str__(self):
        return f"{self.exam_name}-{self.exam_type}"

    class Meta:
        verbose_name = "Exam_Block"

class Studentanswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='student_answers')
    question_number = models.IntegerField()
    answer_text = models.TextField()

    def __str__(self):
        return f"{self.student.username} - Q{self.question_number}: {self.answer_text}"

class Answer(models.Model):
    exam = models.ForeignKey(Exam, related_name="answers", on_delete=models.CASCADE)
    student = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, blank=True)
    question_number = (
        models.IntegerField()
    )  # Indicates which question this answer corresponds to
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
    
    def save(self, *args, **kwargs):
        Studentanswer.objects.create(student=self.student,exam=self.exam, question_number=self.question_number, answer_text=self.answer_text)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("exam", "question_number", "student")


class FullLengthTest(models.Model):
    test_type = models.ForeignKey(
        TestType, on_delete=models.SET_NULL, null=True, help_text="IELTS/PTE etc"
    )
    difficulty_level = models.CharField(max_length=20, choices=Difficulty.choices)
    reading = models.ManyToManyField(
        Exam, limit_choices_to={"exam_type": "Reading"}, related_name="reading"
    )
    listening = models.ManyToManyField(
        Exam, limit_choices_to={"exam_type": "Listening"}, related_name="listening"
    )
    writing = models.ManyToManyField(
        Exam, limit_choices_to={"exam_type": "Writing"}, related_name="writing"
    )
    speaking = models.ManyToManyField(Exam, limit_choices_to={"exam_type": "Speaking"})
