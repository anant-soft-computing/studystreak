# Generated by Django 4.2 on 2024-02-05 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_initial'),
        ('Exam_Responses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='exam.exam'),
        ),
    ]