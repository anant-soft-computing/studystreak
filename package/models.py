# package/models.py

from Courses.models import Course
from django.db import models
from master.models import PackageType


# Section: Package
class Package(models.Model):
    package_name = models.CharField(max_length=255)
    package_price = models.CharField(max_length=100)  # Should this be DecimalField or IntegerField for an actual price?
    PackageType = models.ForeignKey(PackageType, on_delete=models.CASCADE)
    select_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Section: MATERIAL
    soft_copy = models.BooleanField(default=False)
    hard_copy = models.BooleanField(default=False)

    # Section: TESTING
    full_length_test = models.BooleanField(default=False)
    practice_test = models.BooleanField(default=False)
    speaking_test = models.BooleanField(default=False)
    writing_evaluation = models.BooleanField(default=False)
    Total_test = models.IntegerField(default=10)
    # Section: MEMBERSHIP
    live_classes_membership = models.BooleanField(default=False)
    online_membership = models.BooleanField(default=False)
    offline_membership = models.BooleanField(default=False)

    # Section: DOUBT SOLVING
    group_doubt_solving = models.BooleanField(default=False)
    one_to_one_doubt_solving = models.BooleanField(default=False)

    def __str__(self):
        return self.package_name
