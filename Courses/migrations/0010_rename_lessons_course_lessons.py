# Generated by Django 5.0 on 2023-12-14 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0009_remove_course_course_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Lessons',
            new_name='lessons',
        ),
    ]
