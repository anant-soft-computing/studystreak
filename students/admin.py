# students/admin.py

from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
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
        "interested_in_visa_counselling",
    )

    admin.display(empty_value="???")

    def first_name(self, obj):
        return obj.user.first_name if obj.user.first_name else "--"

    def last_name(self, obj):
        return obj.user.last_name if obj.user.first_name else "--"

    empty_value_display = "-empty-"
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

    # # Jazzmin fieldsets
    # fieldsets = (
    #     (
    #         "Basic Info",
    #         {
    #             "fields": (
    #                 "first_name",
    #                 "middle_name",
    #                 "last_name",
    #                 "username",
    #                 # "email",
    #                 "date_of_birth",
    #                 "gender",
    #                 # "password",
    #                 "is_staff",
    #             )
    #         },
    #     ),
    #     (
    #         "Contact Info",
    #         {
    #             "fields": (
    #                 "country",
    #                 "state",
    #                 "city",
    #                 "whatsapp_no",
    #             )
    #         },
    #     ),
    #     (
    #         "Other Info",
    #         {
    #             "fields": (
    #                 "reference_by",
    #                 "country_interested_in",
    #                 "last_education",
    #                 "ielts_taken_before",
    #                 "duolingo_taken_before",
    #                 "pte_taken_before",
    #                 "toefl_taken_before",
    #                 "gre_taken_before",
    #                 "gmat_taken_before",
    #                 "interested_in_visa_counselling",
    #             )
    #         },
    #     ),
    #     ("Login Credential", {"fields": ("email", "password")}),
    #     (
    #         "Course To Enroll",
    #         {
    #             "fields": (
    #                 "course_to_enroll",
    #                 "remark",
    #             )
    #         },
    #     ),
    #     (
    #         "Permissions",
    #         {
    #             "fields": (
    #                 "groups",
    #                 # "user_permissions",
    #             )
    #         },
    #     ),
    # )

    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             # "classes": ("wide",),
    #             "fields": (
    #                 "first_name",
    #                 "username",
    #                 "email",
    #                 "date_of_birth",
    #                 "password1",
    #                 "password2",
    #             ),
    #         },
    #     ),
    # )
    # exclude = (
    #     # "is_superuser",
    #     # "is_staff",
    #     # "groups",
    #     "user_permissions",
    # )

    # readonly_fields = ("last_login",)


admin.site.register(Student, StudentAdmin)

# Register your models here.
