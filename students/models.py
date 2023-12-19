from django.contrib.auth.models import BaseUserManager, User
from django.db import models

# from package.models import Package  # Assuming the City, State, and Country are modeled in the Package app
from master.models import (
    City,  # For the City, State, and Country ForeignKey
    Country,
    State,
)
from package.models import Package


class StudentManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text="Create a student user first and then add the student details",
    )

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHER = "Other", "Other"

    class VisaCounsellingInterest(models.TextChoices):
        YES = "Yes", "Yes"
        NO = "No", "No"

    # Section: Basic Info
    gender = models.CharField(
        max_length=20, choices=Gender.choices, default=Gender.MALE
    )
    country = models.ForeignKey(
        Country, related_name="student_country", on_delete=models.SET_NULL, null=True
    )
    state = models.ForeignKey(
        State, related_name="student_state", on_delete=models.SET_NULL, null=True
    )
    city = models.ForeignKey(
        City, related_name="student_city", on_delete=models.SET_NULL, null=True
    )
    phone_no = models.CharField(max_length=15, null=True)
    whatsapp_no = models.CharField(max_length=15, null=True)
    reference_by = models.TextField( null=True)
    country_interested_in = models.ForeignKey(
        Country,
        related_name="student_interest_country",
        on_delete=models.SET_NULL,
        null=True,
    )
    last_education = models.CharField(max_length=200, null=True)
    ielts_taken_before = models.BooleanField(default=False)
    duolingo_taken_before = models.BooleanField(default=False)
    pte_taken_before = models.BooleanField(default=False)
    toefl_taken_before = models.BooleanField(default=False)
    gre_taken_before = models.BooleanField(default=False)
    gmat_taken_before = models.BooleanField(default=False)
    remark = models.TextField( null=True)
    biography = models.TextField( null=True)  # If you're using django-ckeditor or similar, this can be replaced with RichTextField
    user_image = models.ImageField(upload_to="student_images/", null=True)
    interested_in_visa_counselling = models.CharField(
        max_length=50,
        choices=VisaCounsellingInterest.choices,
        default=VisaCounsellingInterest.YES,
        null=True
    )
    course_to_enroll = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    create_batch = models.ForeignKey(
        "master.batch",
        on_delete=models.CASCADE,
        null=True
    )
    create_course = models.ForeignKey(
        "Courses.Course",
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super().delete(*args, **kwargs)
