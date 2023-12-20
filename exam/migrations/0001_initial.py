# Generated by Django 4.2 on 2023-12-20 07:18

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0021_examtype_questiontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_Name', models.CharField(max_length=10)),
                ('passage', froala_editor.fields.FroalaField()),
                ('no_of_questions', models.IntegerField(default=4)),
                ('question', froala_editor.fields.FroalaField()),
                ('exam_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.examtype')),
                ('question_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.questiontype')),
            ],
            options={
                'verbose_name': 'Exam_Block',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('answer_text', models.TextField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exam.exam')),
            ],
            options={
                'unique_together': {('exam', 'question_number')},
            },
        ),
    ]