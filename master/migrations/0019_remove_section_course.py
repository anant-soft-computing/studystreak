# Generated by Django 4.2 on 2023-12-19 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0018_additionalresource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='course',
        ),
    ]
