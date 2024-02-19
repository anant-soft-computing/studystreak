from django.contrib import admin
from exam.models import Studentanswer  # Import the StudentAnswer model from your app

class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'question_number', 'answer_text')

# Register your models with the admin site
admin.site.register(Studentanswer, StudentAnswerAdmin)
