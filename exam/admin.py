from django.contrib import admin

from .models import Answer, Exam

# Register your models here.


class AnswerInline(admin.TabularInline):
    """Tabular Inline View for Answer"""

    model = Answer
    extra = 1
    fk_name = "exam"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "exam_Name",
                    "exam_type",
                ),
            },
        ),
        (
            "Block details",
            {
                "fields": (
                    "block_type",
                    "difficulty_level",
                    "block_threshold",
                ),
            },
        ),
        (
            "Question details",
            {
                "fields": (
                    "question_type",
                    "passage",
                    "no_of_questions",
                    "question",
                ),
            },
        ),
    )
