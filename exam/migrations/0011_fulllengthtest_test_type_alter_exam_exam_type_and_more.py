# Generated by Django 4.2 on 2023-12-22 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0023_testtype'),
        ('exam', '0010_exam_test_type_alter_exam_exam_type_fulllengthtest'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulllengthtest',
            name='test_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.testtype'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_type',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Listening', 'Listening'), ('Speaking', 'Speaking'), ('Writing', 'Writing')], default='Reading', help_text='(Reading, Listening, Speaking, Writing)', max_length=20),
        ),
        migrations.AlterField(
            model_name='fulllengthtest',
            name='writing',
            field=models.ManyToManyField(limit_choices_to={'exam_type': 'Writing'}, related_name='writing', to='exam.exam'),
        ),
    ]
