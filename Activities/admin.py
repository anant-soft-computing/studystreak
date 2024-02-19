from django.contrib import admin
from django.contrib import admin
from .models import UserCoursesActivity, UserLessonsActivity,UserassessmentActivity,UserQuizActivity,UserFullLengthTestActivity

# Register your models here
admin.site.register(UserCoursesActivity)
admin.site.register(UserLessonsActivity)
admin.site.register(UserassessmentActivity)
admin.site.register(UserQuizActivity)
#admin.site.register(UserExam_BlockTestActivity)
admin.site.register(UserFullLengthTestActivity)

