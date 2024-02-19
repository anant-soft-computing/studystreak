from django.db import models
from master.models import batch
from Courses.models import Course

class LiveClass(models.Model):
    batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True, blank=True)
    meeting_title = models.CharField(max_length=255)
    meeting_description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    zoom_meeting_id = models.CharField(max_length=100, blank=True, null=True)
    zoom_meeting_password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.meeting_title

    class Meta:
        verbose_name_plural = "LiveClasses"
