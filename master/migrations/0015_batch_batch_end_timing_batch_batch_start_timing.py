# Generated by Django 4.2 on 2023-12-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_rename_add_course_batch_create_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='batch_end_timing',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='batch_start_timing',
            field=models.TimeField(blank=True, null=True),
        ),
    ]