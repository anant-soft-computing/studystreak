# students/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Student


class StudentAdmin(ImportExportModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "course_to_enroll",
        "whatsapp_no",
        "last_education",
        "ielts_taken_before",
        "duolingo_taken_before",
        "pte_taken_before",
        "toefl_taken_before",
        "country_interested_in",
        "remark",
        "email",
        "interested_in_visa_counselling",
    )
    search_fields = ["first_name", "last_name", "email"]
    list_filter = [
        "course_to_enroll",
        "gender",
        "country_interested_in",
        "state",
        "city",
        "ielts_taken_before",
        "duolingo_taken_before",
        "pte_taken_before",
        "toefl_taken_before",
        "gre_taken_before",
        "gmat_taken_before",
        "interested_in_visa_counselling",
    ]

    # Jazzmin fieldsets
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    # "email",
                    "date_of_birth",
                    "gender",
                    # "password",
                )
            },
        ),
        (
            "Contact Info",
            {
                "fields": (
                    "country",
                    "state",
                    "city",
                    "whatsapp_no",
                )
            },
        ),
        (
            "Other Info",
            {
                "fields": (
                    "reference_by",
                    "country_interested_in",
                    "last_education",
                    "ielts_taken_before",
                    "duolingo_taken_before",
                    "pte_taken_before",
                    "toefl_taken_before",
                    "gre_taken_before",
                    "gmat_taken_before",
                    "interested_in_visa_counselling",
                )
            },
        ),
        ("Login Credential", {"fields": ("email", "password")}),
        (
            "Course To Enroll",
            {
                "fields": (
                    "course_to_enroll",
                    "remark",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    # "groups",
                    "user_permissions",
                )
            },
        ),
    )

    exclude = (
        "is_superuser",
        "is_staff",
        "groups",
    )

    readonly_fields = ("last_login",)


admin.site.register(Student, StudentAdmin)

# Register your models here.
