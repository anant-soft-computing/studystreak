# Generated by Django 5.0 on 2023-12-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='name',
            field=models.TimeField(max_length=200),
        ),
    ]
