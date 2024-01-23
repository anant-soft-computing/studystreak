import nested_admin
from django.contrib import admin
from nested_admin import NestedModelAdmin

from master.models import LessonAssignment, LessonAttachment

from .models import Lesson


# class LessonAssignmentInline(nested_admin.NestedStackedInline):
#     model = LessonAssignment
#     extra = 1
#     fk_name = "lesson"


class LessonAttachmentInline(nested_admin.NestedStackedInline):
    model = LessonAttachment
    extra = 1
    fk_name = "lesson"


# class QuizOptionAdmin(admin.ModelAdmin):
#     # model = QuizOption
#     list_display = ['name', 'Answers', 'correct_answer']
#     list_filter = ['name']
# admin.site.register(QuizOption, QuizOptionAdmin)
#     # extra = 1


# class QuestionInline(nested_admin.NestedStackedInline):
#     model = Quiz_Question
#     extra = 2
#     # fk_name = 'name'
#     inlines = [OptionsInline]


class Quiz_QuestionAdmin(NestedModelAdmin):
    model = Lesson
    list_display = [
        "section",
        "Lesson_Title",
        "Lesson_Description",
        "Lesson_Video",
        "Lesson_Duration",
        "active",
    ]
    list_filter = [
        "section",
        "Lesson_Title",
        "Lesson_Description",
        "Lesson_Video",
        "Lesson_Duration",
        "active",
    ]
    search_fields = ["Lesson_Title"]
    inlines = [LessonAttachmentInline]


admin.site.register(Lesson, Quiz_QuestionAdmin)

# class Quiz_QuestionAdmin(admin.ModelAdmin):
#     # model = Lesson
#     list_display = ['Question', 'lesson',]
#     list_filter = ['Question', 'lesson',]
#     # search_fields = ['Lesson_Title']
#     # inlines = [QuestionInline]

# admin.site.register(Quiz_Question, Quiz_QuestionAdmin)

# class SiteAddressInline(admin.StackedInline):
#     model = SiteAddress


# @admin.register(Site)
# class SiteAdmin(admin.ModelAdmin):
#     inlines = [BillingAddressInline, SiteAddressInline, ContactInline]
