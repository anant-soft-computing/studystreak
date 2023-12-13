# Generated by Django 5.0 on 2023-12-11 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lesson_Title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('Lesson_Description', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('Lesson_Video', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('Lesson_Duration', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('Lesson_attachment', models.FileField(blank=True, default=None, null=True, upload_to='documents/')),
                ('active', models.BooleanField(default=False)),
                ('section', models.ForeignKey(blank=True, default=None, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.section')),
            ],
        ),
    ]
