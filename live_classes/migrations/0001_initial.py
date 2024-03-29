# Generated by Django 4.2 on 2024-02-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_title', models.CharField(max_length=255)),
                ('meeting_description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('zoom_meeting_id', models.CharField(blank=True, max_length=100, null=True)),
                ('zoom_meeting_password', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'LiveClasses',
            },
        ),
    ]
