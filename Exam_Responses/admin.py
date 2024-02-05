from django.contrib import admin
from .models import StudentAnswer, Student_Answer

# Register your models here.





class AnswerInline(admin.TabularInline):
    """Tabular Inline View for Answer"""

    model = Student_Answer
    extra = 1
    fk_name = "student_exam"

class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "user",)
    inlines = [AnswerInline]
admin.site.register(StudentAnswer, StudentAnswerAdmin)