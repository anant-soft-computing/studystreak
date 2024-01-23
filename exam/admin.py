from django.contrib import admin

from .models import Answer, Exam, FullLengthTest

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
    list_display = ['exam_name', 'exam_type']
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "exam_name",
                    "exam_type",
                    "type_of_module",
                    "test_type",
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


@admin.register(FullLengthTest)
class FullLengthTestAdmin(admin.ModelAdmin):
    pass
