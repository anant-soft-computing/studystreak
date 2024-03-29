# Generated by Django 4.2 on 2024-02-08 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exam', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentanswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='exam.exam')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField()),
                ('answer_text', models.TextField()),
                ('student_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_exam', to='ExamResponses.studentanswer')),
            ],
        ),
    ]
