# students/admin.py

from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'course_to_enroll', 'whatsapp_no', 'last_education', 'ielts_taken_before', 'duolingo_taken_before', 'pte_taken_before',
                    'toefl_taken_before','country_interested_in', 'remark' , 'email', 'interested_in_visa_counselling')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['course_to_enroll', 'gender', 'country_interested_in', 'state', 'city', 'ielts_taken_before', 'duolingo_taken_before',
                   'pte_taken_before', 'toefl_taken_before', 'gre_taken_before', 'gmat_taken_before', 'interested_in_visa_counselling']

    # Jazzmin fieldsets
    fieldsets = (
        ('Basic Info', {
            'fields': ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender',)
        }),

        ('Contact Info', {
            'fields': ('country', 'state', 'city', 'whatsapp_no',)
        }),

        ('Other Info', {
            'fields': (
                'reference_by', 'country_interested_in', 'last_education', 'ielts_taken_before',
                'duolingo_taken_before',
                'pte_taken_before', 'toefl_taken_before', 'gre_taken_before', 'gmat_taken_before',
                'interested_in_visa_counselling')
        }),

        ('Login Credential', {
            'fields': ('email', 'password')
        }),

        ('Course To Enroll', {
            'fields': ('course_to_enroll', 'remark',)
        }),
    )


admin.site.register(Student, StudentAdmin)

# Register your models here.
