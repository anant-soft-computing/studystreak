# Generated by Django 4.2 on 2024-02-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Create_Test', '0005_alter_responses_responses_listening_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='exam_test',
            field=models.CharField(choices=[('Practice', 'Practice'), ('Full Length', 'Full Length')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='module_category',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
