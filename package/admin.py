# # package/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Package

# from master.models import PackageType


class PackageAdmin(ImportExportModelAdmin):
    list_display = [
        "package_name",
        "package_price",
        "PackageType",
        "soft_copy",
        "hard_copy",
        "full_length_test",
        "practice_test",
        "speaking_test",
        "writing_evaluation",
        "Total_test",
        "live_classes_membership",
        "group_doubt_solving",
        "one_to_one_doubt_solving",
        "select_course",
    ]
    list_filter = [
        "PackageType",
        "soft_copy",
        "hard_copy",
        "full_length_test",
        "practice_test",
        "speaking_test",
        "writing_evaluation",
        "Total_test",
        "live_classes_membership",
        "group_doubt_solving",
        "one_to_one_doubt_solving",
        "select_course",
    ]
    search_fields = ["package_name"]

    # Jazzmin fieldsets
    fieldsets = (
        (
            "Package",
            {
                "fields": (
                    "package_name",
                    "package_price",
                    "PackageType",
                    "select_course",
                )
            },
        ),
        ("MATERIAL", {"fields": ("soft_copy", "hard_copy")}),
        (
            "TESTS",
            {
                "fields": (
                    "full_length_test",
                    "practice_test",
                    "speaking_test",
                    "writing_evaluation",
                    "Total_test",
                )
            },
        ),
        (
            "MEMBERSHIP",
            {
                "fields": (
                    "live_classes_membership",
                    "online_membership",
                    "offline_membership",
                )
            },
        ),
        (
            "DOUBT SOLVING",
            {"fields": ("group_doubt_solving", "one_to_one_doubt_solving")},
        ),
    )


admin.site.register(Package, PackageAdmin)
