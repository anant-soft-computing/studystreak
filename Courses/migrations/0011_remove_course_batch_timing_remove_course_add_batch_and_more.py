# Generated by Django 4.2 on 2023-12-18 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0010_rename_lessons_course_lessons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Batch_Timing',
        ),
        migrations.RemoveField(
            model_name='course',
            name='add_batch',
        ),
        migrations.RemoveField(
            model_name='course',
            name='add_package',
        ),
    ]