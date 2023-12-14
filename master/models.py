# master/models.py
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Requirements(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]  # Displaying the first 50 characters
    class Meta:
        verbose_name_plural = "Requirements"

class Outcomes(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]  # Displaying the first 50 characters
    class Meta:
        verbose_name_plural = "Outcomes"

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CourseOverview(models.Model):
    overview = models.TextField()

    def __str__(self):
        return self.overview[:50]  # Displaying the first 50 characters


class SEOMetakeywords(models.Model):
    keywords = ArrayField(models.SlugField(max_length=200), blank=True)

    def __str__(self):
        return " ".join(tag for tag in self.keywords)
    
    class Meta:
        verbose_name_plural = "SEOMetakeywords"


class PackageType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey("Courses.Course", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class batch(models.Model):
    batch_name = models.CharField(max_length=200, null=True, blank=True)
    batch_startdate = models.DateField(null=True, blank=True)
    batch_enddate = models.DateField(null=True, blank=True)
    batch_timing = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.batch_name


class Attachment(models.Model):
    attachment = models.FileField(
        upload_to="documents/", null=True, blank=True, default=None
    )
    attachment_description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default=None,
        verbose_name="Attachment Description",
    )

    class Meta:
        abstract = True


class LessonAttachment(Attachment):
    lesson = models.ForeignKey("coursedetail.Lesson", on_delete=models.CASCADE)


class LessonAssignment(Attachment):
    lesson = models.ForeignKey("coursedetail.Lesson", on_delete=models.CASCADE)
