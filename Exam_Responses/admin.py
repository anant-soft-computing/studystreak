from django.contrib import admin
from .models import StudentAnswer

# Register your models here.


class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "exam", "question_number",)
    
admin.site.register(StudentAnswer, StudentAnswerAdmin)


