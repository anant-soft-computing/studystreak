# Generated by Django 5.0 on 2023-12-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
