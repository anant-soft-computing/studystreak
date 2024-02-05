# Generated by Django 4.2 on 2024-02-05 12:28

import ckeditor.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Title', models.CharField(max_length=200)),
                ('Short_Description', ckeditor.fields.RichTextField()),
                ('Description', ckeditor.fields.RichTextField()),
                ('EnrollmentStartDate', models.DateField()),
                ('EnrollmentEndDate', models.DateField()),
                ('max_enrollments', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('faqs', ckeditor.fields.RichTextField()),
                ('Featured', models.BooleanField(default=False)),
                ('Support_Available', models.BooleanField(default=False)),
                ('Course_Overview_Provider', models.CharField(max_length=200)),
                ('Course_Overview_URL', models.URLField()),
                ('Course_Thumbnail', models.ImageField(upload_to='course_thumbnails/')),
                ('SEO_Meta_Keywords', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(max_length=200), blank=True, size=None)),
                ('Meta_Description', django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(max_length=200), blank=True, size=None)),
                ('course_delivery', models.CharField(blank=True, choices=[('TAUGHT', 'Taught course'), ('SELF-STUDY', 'Self-study course')], max_length=200, null=True)),
                ('course_type', models.CharField(blank=True, choices=[('PRIVATE', 'PRIVATE'), ('PUBLIC', 'PUBLIC')], max_length=200, null=True)),
                ('course_identifier', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
    ]
