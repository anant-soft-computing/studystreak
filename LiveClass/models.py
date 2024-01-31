from django.db import models
from master.models import batch, Live_Class_Type
from Courses.models import Course 
from django.contrib.auth.models import User
class Live_Class(models.Model):
    select_batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True, blank=True)
    live_class_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    liveclasstype = models.ForeignKey(Live_Class_Type, on_delete=models.CASCADE)
    meeting_title = models.CharField(max_length=255)
    meeting_description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    zoom_meeting_id = models.CharField(max_length=100, blank=True, null=True)
    zoom_meeting_password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.meeting_title