# Generated by Django 4.2 on 2024-01-31 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exam', '0017_exam_exam_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Listening', models.ManyToManyField(blank=True, null=True, related_name='listening+', to='exam.exam')),
                ('Reading', models.ManyToManyField(blank=True, null=True, related_name='reading+', to='exam.exam')),
                ('Speaking', models.ManyToManyField(blank=True, null=True, related_name='Speaking+', to='exam.exam')),
                ('Writing', models.ManyToManyField(blank=True, null=True, related_name='writing+', to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='createexam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IELTS', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Create_Test.module')),
            ],
        ),
    ]