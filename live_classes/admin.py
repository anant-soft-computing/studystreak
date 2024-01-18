# live_classes/admin.py

from django.contrib import admin
from .models import LiveClass

class LiveClassAdmin(admin.ModelAdmin):
    list_display = ['meeting_title', 'start_time', 'end_time']
    list_filter = ['start_time', 'end_time']
    search_fields = ['meeting_title']
    ordering = ['start_time']

admin.site.register(LiveClass, LiveClassAdmin)
