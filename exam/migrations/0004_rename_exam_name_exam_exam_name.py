# Generated by Django 4.2 on 2023-12-21 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_alter_exam_passage_alter_exam_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='exam_Name',
            new_name='exam_name',
        ),
    ]
