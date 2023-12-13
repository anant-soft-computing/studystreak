# Courses/models.py

from django.db import models
from master.models import Category, Level, Requirements, Outcomes, Language, batch
from coursedetail.models import Lesson

class Course(models.Model):
    # Course Detail
    Course_Title = models.CharField(max_length=200)
    Short_Description = models.TextField()
    Description = models.TextField()  # If using a rich-text editor like CKEditor, this will be a RichTextField instead
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
    Requirements = models.ForeignKey(Requirements, on_delete=models.CASCADE)

    #Batch Timing

    Batch_Timing = models.ForeignKey(batch,max_length=200,on_delete=models.CASCADE)

    # Outcome
    Outcome = models.ManyToManyField(Outcomes)

    # Course Price
    Course_Price = models.PositiveIntegerField()
    Discount_in_percent = models.PositiveIntegerField()

    # Course Media
    Course_Overview_Provider = models.CharField(max_length=200)
    Course_Overview_URL = models.URLField()
    Course_Thumbnail = models.ImageField(upload_to='course_thumbnails/')
    course_material = models.CharField(max_length=200,  null=True, blank=True)
    # Course SEO
    SEO_Meta_Keywords = models.TextField()
    Meta_Description = models.TextField()

    #Lessons
    Lessons = models.ManyToManyField(Lesson, blank=True)

    # Django requires this for the admin site

    def __str__(self):
        return self.Course_Title



 
