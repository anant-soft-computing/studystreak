# students/admin.py

import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from import_export.admin import ExportMixin

from .models import Student


class StudentAdmin(ExportMixin, admin.ModelAdmin):
    ordering = ("-created_at",)
    date_hierarchy = "created_at"

    def changelist_view(self, request, extra_content=None):
        response = super().changelist_view(request, extra_context=extra_content)
        queryset = response.context_data["cl"].queryset
        chart_data = self.chart_data(queryset)
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        response.context_data.update({"chart_data": as_json})
        return response

    def chart_data(self, queryset):
        return (
            queryset.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

    import_export_change_list_template = (
        "admin/students/student/change_list_export.html"
    )
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
        "create_batch",
        "create_course",
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
        "create_batch",
        "create_course",
    ]

    search_fields = (
        "user__first_name",
        "user__last_name",
    )
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
