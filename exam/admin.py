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
