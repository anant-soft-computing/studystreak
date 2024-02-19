# Generated by Django 5.0 on 2023-12-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0007_remove_course_requirements_course_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_delivery',
            field=models.CharField(blank=True, choices=[('TAUGHT', 'Taught course'), ('SELF-STUDY', 'Self-study course')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(blank=True, choices=[('PRIVATE', 'PRIVATE'), ('PUBLIC', 'PUBLIC')], max_length=200, null=True),
        ),
    ]