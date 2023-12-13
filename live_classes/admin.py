# live_classes/admin.py

from django.contrib import admin
from .models import LiveClass

class LiveClassAdmin(admin.ModelAdmin):
    list_display = ['course', 'meeting_title', 'start_time', 'end_time',]
    list_filter = ['course', 'start_time', 'end_time', 'meeting_title', ]
    search_fields = ['meeting_title', 'course__course_title']
    ordering = ['start_time']

admin.site.register(LiveClass, LiveClassAdmin)
