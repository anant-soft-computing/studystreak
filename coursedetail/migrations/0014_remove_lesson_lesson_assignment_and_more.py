# Generated by Django 4.2 on 2024-01-23 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetail', '0013_lesson_lesson_assignment_lesson_lesson_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_assignment',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_quiz',
        ),
    ]
