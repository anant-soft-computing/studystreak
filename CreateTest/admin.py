# from django.contrib import admin
# from .models import *
# from nested_admin import NestedTabularInline, NestedModelAdmin
# # Register your models here.


# admin.site.register(createexam)
# admin.site.register(module)
# admin.site.register(ReadingQuestionTypeName)
# admin.site.register(ReadingPassageName)


# class OptionsInline(NestedTabularInline):
#     model = Options
#     extra = 1
    
# class QuestionInline(NestedTabularInline):
#     model = Question
#     extra = 1
#     fk_name = 'name'
#     inlines = [OptionsInline]
    
# class ReadingQuestionAdmin(NestedModelAdmin):
#     model = ReadingQuestion
#     inlines = [QuestionInline]

# admin.site.register(ReadingQuestion, ReadingQuestionAdmin) 