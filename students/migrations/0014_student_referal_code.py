# Generated by Django 4.2 on 2023-12-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_alter_student_biography_alter_student_create_batch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='referal_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
