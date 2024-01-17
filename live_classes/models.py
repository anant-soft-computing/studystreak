# live_classes/models.py

from django.db import models

from Courses.models import Course
from master.models import LiveClassType

class LiveClass(models.Model):
    # live_class_name = models.CharField(max_length=200, null=True,blank=True)
    # live_class_type = models.ForeignKey(LiveClassType, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    package = models.ForeignKey(
        "package.Package", on_delete=models.CASCADE, null=True, blank=True
    )
    batch = models.ForeignKey(
        "master.batch", on_delete=models.CASCADE, null=True, blank=True
    )
    meeting_title = models.CharField(max_length=255)
    meeting_description = models.TextField()  # If you're using django-ckeditor or similar, this can be replaced with RichTextField
    start_time = models.TimeField()
    end_time = models.TimeField()
    zoom_meeting_id = models.CharField(max_length=100, null=True)
    zoom_meeting_password = models.CharField(max_length=100)

    def __str__(self):
        return self.meeting_title

    class Meta:
        verbose_name_plural = "LiveClasses"
