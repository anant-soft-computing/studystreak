# master/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (
    Category,
    City,
    Country,
    CourseOverview,
    Cupon,
    ExamType,
    Language,
    Level,
    Outcomes,
    PackageType,
    QuestionType,
    Requirements,
    Section,
    SEOMetakeywords,
    State,
    batch,
)


@admin.register(ExamType)
class ExamTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Level)
class LevelAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Requirements)
class RequirementsAdmin(ImportExportModelAdmin):
    list_display = ["description"]
    search_fields = ["description"]


@admin.register(Outcomes)
class OutcomesAdmin(ImportExportModelAdmin):
    list_display = ["description"]
    search_fields = ["description"]


@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(CourseOverview)
class CourseOverviewAdmin(ImportExportModelAdmin):
    list_display = ["overview"]
    search_fields = ["overview"]


@admin.register(SEOMetakeywords)
class SEOMetakeywordsAdmin(ImportExportModelAdmin):
    list_display = ["keywords"]
    search_fields = ["keywords"]


@admin.register(PackageType)
class PackageTypeAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(batch)
class batchAdmin(ImportExportModelAdmin):
    list_display = [
        "batch_name",
        "batch_startdate",
        "batch_enddate",
        "batch_start_timing",
        "batch_end_timing",
    ]
    search_fields = [
        "batch_name",
        "batch_startdate",
        "batch_enddate",
        "batch_start_timing",
        "batch_end_timing",
    ]


@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    pass
