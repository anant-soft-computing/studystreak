# Generated by Django 4.2 on 2023-12-14 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_batch_batch_end_timing_batch_batch_start_timing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='batch_timing',
        ),
    ]
