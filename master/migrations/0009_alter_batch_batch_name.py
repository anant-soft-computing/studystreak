# Generated by Django 5.0 on 2023-12-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_alter_seometakeywords_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]