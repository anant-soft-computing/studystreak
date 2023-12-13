# Generated by Django 5.0 on 2023-12-13 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetail', '0009_remove_lesson_lesson_attachment'),
        ('master', '0005_lessonattachment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonattachment',
            old_name='Lesson_attachment',
            new_name='attachment',
        ),
        migrations.RemoveField(
            model_name='lessonattachment',
            name='Lesson_attachment_description',
        ),
        migrations.AddField(
            model_name='lessonattachment',
            name='attachment_description',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Attachment Description'),
        ),
        migrations.CreateModel(
            name='LessonAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, default=None, null=True, upload_to='documents/')),
                ('attachment_description', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Attachment Description')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursedetail.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
