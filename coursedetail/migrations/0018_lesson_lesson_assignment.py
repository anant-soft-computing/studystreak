# Generated by Django 4.2 on 2024-01-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0016_alter_exam_block_type'),
        ('coursedetail', '0017_delete_assignment_answer_delete_assignment_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_assignment',
            field=models.ManyToManyField(related_name='lesson_assignment', to='exam.exam'),
        ),
    ]
