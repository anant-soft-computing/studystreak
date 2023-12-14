# Courses/models.py

from django.contrib.postgres.fields import ArrayField
from django.db import models

from coursedetail.models import Lesson
from master.models import Category, Language, Level, Outcomes, Requirements, batch


class course_type(models.TextChoices):
    private = "PRIVATE", "PRIVATE"
    public = "PUBLIC", "PUBLIC"


class course_delivery(models.TextChoices):
    taught = "TAUGHT", "Taught course"
    self_study = "SELF-STUDY", "Self-study course"


class Course(models.Model):
    # Course Detail
    Course_Title = models.CharField(max_length=200)
    Short_Description = models.TextField()
    Description = (
        models.TextField()
    )  # If using a rich-text editor like CKEditor, this will be a RichTextField instead
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Level = models.ForeignKey(Level, on_delete=models.CASCADE)
    Language = models.ForeignKey(Language, on_delete=models.CASCADE)
    EnrollmentStartDate = models.DateField()
    EnrollmentEndDate = models.DateField()
    enrollment_count = models.IntegerField(default=0)
    max_enrollments = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    faqs = models.TextField(null=True, blank=True)
    Featured = models.BooleanField(default=False)
    Support_Available = models.BooleanField(default=False)

    # Requirements
    Requirements = models.ManyToManyField(Requirements)

    # Batch Timing

    Batch_Timing = models.ForeignKey(batch, max_length=200, on_delete=models.CASCADE)

    # Outcome
    Outcome = models.ManyToManyField(Outcomes)

    # Course Price
    # Course_Price = models.PositiveIntegerField()
    # Discount_in_percent = models.PositiveIntegerField()

    # Course Media
    Course_Overview_Provider = models.CharField(max_length=200)
    Course_Overview_URL = models.URLField()
    Course_Thumbnail = models.ImageField(upload_to="course_thumbnails/")
    course_material = models.CharField(max_length=200, null=True, blank=True)
    # Course SEO
    SEO_Meta_Keywords = ArrayField(models.SlugField(max_length=200), blank=True)
    Meta_Description = ArrayField(models.SlugField(max_length=200), blank=True)
    # Lessons
    Lessons = models.ManyToManyField(Lesson, blank=True)

    course_delivery = models.CharField(
        max_length=200, null=True, blank=True, choices=course_delivery.choices
    )
    course_type = models.CharField(
        max_length=200, null=True, blank=True, choices=course_type.choices
    )
    # Django requires this for the admin site
    add_batch = models.ForeignKey('master.batch', on_delete = models.CASCADE, related_name = "+")
    add_package  = models.ForeignKey('package.Package', on_delete = models.CASCADE)
    

    def __str__(self):
        return self.Course_Title
