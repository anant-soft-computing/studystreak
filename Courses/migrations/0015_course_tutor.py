# Generated by Django 4.2 on 2023-12-19 10:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses', '0014_course_course_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ManyToManyField(null=True, related_name='tutor', to=settings.AUTH_USER_MODEL),
        ),
    ]
