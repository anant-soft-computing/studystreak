# master/models.py
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


class Outcomes(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]  # Displaying the first 50 characters


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CourseOverview(models.Model):
    overview = models.TextField()

    def __str__(self):
        return self.overview[:50]  # Displaying the first 50 characters


class SEOMetakeywords(models.Model):
    keywords = models.TextField()

    def __str__(self):
        return self.keywords[:50]  # Displaying the first 50 characters


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
    batch_name = models.TimeField(max_length=200, null=True, blank=True)
    batch_startdate = models.DateField(null=True, blank=True)
    batch_enddate = models.DateField(null=True, blank=True)
    batch_timing = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.batch_name
