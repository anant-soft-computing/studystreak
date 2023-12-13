from django.db import models
#from package.models import Package  # Assuming the City, State, and Country are modeled in the Package app
from Courses.models import Course  # For the Course To Enroll ForeignKey
from master.models import City, State, Country  # For the City, State, and Country ForeignKey
from package.models import Package

class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'
        OTHER = 'Other', 'Other'
        # ... you can add more choices as needed

    class VisaCounsellingInterest(models.TextChoices):
        YES = 'Yes', 'Yes'
        NO = 'No', 'No'
        # ... additional choices if needed

    # Section: Basic Info
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.MALE)
    country = models.ForeignKey(Country, related_name="student_country", on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, related_name="student_state", on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, related_name="student_city", on_delete=models.SET_NULL, null=True)
    phone_no = models.CharField(max_length=15)
    whatsapp_no = models.CharField(max_length=15)
    reference_by = models.TextField()
    country_interested_in = models.ForeignKey(Country, related_name="student_interest_country", on_delete=models.SET_NULL, null=True)
    last_education = models.CharField(max_length=200)
    ielts_taken_before = models.BooleanField(default=False)
    duolingo_taken_before = models.BooleanField(default=False)
    pte_taken_before = models.BooleanField(default=False)
    toefl_taken_before = models.BooleanField(default=False)
    gre_taken_before = models.BooleanField(default=False)
    gmat_taken_before = models.BooleanField(default=False)
    remark = models.TextField()
    biography = models.TextField()  # If you're using django-ckeditor or similar, this can be replaced with RichTextField
    user_image = models.ImageField(upload_to='student_images/')
    interested_in_visa_counselling = models.CharField(max_length=50, choices=VisaCounsellingInterest.choices, default=VisaCounsellingInterest.YES)
    # Section: Login Credential
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Storing password as CharField is not safe. Normally, you'd use Django's User model or a custom user model for handling authentication.

    # Course To Enroll
    course_to_enroll = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
