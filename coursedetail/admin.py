import nested_admin
from django.contrib import admin
from nested_admin import NestedModelAdmin

from .models import Lesson, Quiz_Question, QuizOption


class OptionsInline(nested_admin.NestedStackedInline):
    model = QuizOption
    extra = 1


class QuestionInline(nested_admin.NestedStackedInline):
    model = Quiz_Question
    extra = 2
    # fk_name = 'name'
    inlines = [OptionsInline]


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
    inlines = [QuestionInline]


admin.site.register(Lesson, Quiz_QuestionAdmin)

# class Quiz_QuestionAdmin(NestedModelAdmin):
#     model = Lesson
#     list_display = ['section', 'Lesson_Title', 'Lesson_Description', 'Lesson_Video', 'Lesson_Duration', 'Lesson_attachment', 'active']
#     list_filter = ['section', 'Lesson_Title', 'Lesson_Description', 'Lesson_Video', 'Lesson_Duration', 'Lesson_attachment', 'active']
#     search_fields = ['Lesson_Title']
#     inlines = [QuestionInline]

# admin.site.register(Lesson, Quiz_QuestionAdmin)

# class SiteAddressInline(admin.StackedInline):
#     model = SiteAddress


# @admin.register(Site)
# class SiteAdmin(admin.ModelAdmin):
#     inlines = [BillingAddressInline, SiteAddressInline, ContactInline]
