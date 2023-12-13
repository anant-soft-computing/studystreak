# Courses/admin.py

from django.contrib import admin
from .models import Course
from import_export.admin import ImportExportModelAdmin





@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ['Course_Title', 'Category', 'Level', 'Language', 'EnrollmentStartDate', 'EnrollmentEndDate','enrollment_count','is_active','Featured',
                    'Support_Available' , 'Course_Price', 'Discount_in_percent', 'faqs','Course_Overview_Provider',
                    'Course_Overview_URL', 'Course_Thumbnail', 'SEO_Meta_Keywords', 'Meta_Description']
    list_filter = ['Category', 'Level', 'Language', 'EnrollmentStartDate', 'EnrollmentEndDate','enrollment_count','is_active','faqs','Featured', 'Support_Available'
                   , 'Course_Price', 'Discount_in_percent', 'Course_Overview_Provider', 'Course_Overview_URL',
                   'Course_Thumbnail', 'SEO_Meta_Keywords', 'Meta_Description']
    search_fields = ['Course_Title', 'Short_Description', 'Description', 'Category', 'Level', 'Language', 'EnrollmentStartDate', 'EnrollmentEndDate','enrollment_count','is_active','faqs','Lessons']

    # Using fieldsets to organize the admin form into sections/tabs as per Jazzmin theme
    fieldsets = (
        ("Course Detail", {
            "fields": (
            'Course_Title', 'Short_Description', 'Description', 'Category', 'Level', 'Language', 'EnrollmentStartDate', 'EnrollmentEndDate','enrollment_count','Featured',
            'Support_Available')
        }),
        ("Requirements", {
            "fields": ('Requirements',),
        }),

        ("Batch Timing", {
            "fields": ('Batch_Timing',),
        }),

        ("Outcome", {
            "fields": ('Outcome',),
        }),
        ("Course Price", {
            "fields": ('Course_Price', 'Discount_in_percent'),
        }),
        ("Course Media", {
            "fields": ('Course_Overview_Provider', 'Course_Overview_URL', 'Course_Thumbnail'),
        }),
        ("Course SEO", {
            "fields": ('SEO_Meta_Keywords', 'Meta_Description'),
        }),
        ("Course Lessons", {
            "fields": ('Lessons',),
        }),
    )


# admin.site.register()