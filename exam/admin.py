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
                    "exam_name",
                    "exam_type",
                    "type_of_module",
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
                    "audio_file",
                    "passage",
                    "no_of_questions",
                    "question",
                ),
            },
        ),
    )
