# Generated by Django 4.2 on 2024-01-31 14:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Create_Test', '0004_remove_responses_exam_responses_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responses',
            name='responses_listening',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(max_length=500), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='responses',
            name='responses_reading',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(max_length=500), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='responses',
            name='responses_speaking',
            field=models.FileField(blank=True, null=True, upload_to='responses_audio/'),
        ),
        migrations.AlterField(
            model_name='responses',
            name='responses_writing',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SlugField(max_length=500), blank=True, null=True, size=None),
        ),
    ]
