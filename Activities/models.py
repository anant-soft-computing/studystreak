from django.db import models
from django.contrib.auth.models import User
from Courses.models import Course
from coursedetail.models import Lesson
from assessment.models import assessment
from exam.models import FullLengthTest
#from exam.models import Exam_Block

class UserCoursesActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Courses = models.ManyToManyField(Course, blank=True)
    status = models.CharField(max_length=100)

class UserLessonsActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, blank=True)
    status = models.CharField(max_length=100)

class UserassessmentActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, blank=True)
    status = models.CharField(max_length=100)

class UserQuizActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, blank=True)
    status = models.CharField(max_length=100)

class UserFullLengthTestActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Courses = models.ManyToManyField(Course, blank=True)
    status = models.CharField(max_length=100)

# class UserExam_BlockTestActivity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Courses = models.ManyToManyField(Course, blank=True)
#     status = models.CharField(max_length=100)
