# Generated by Django 4.2 on 2024-01-26 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_gamification', '0015_alter_badgedefinition_name_and_more'),
        ('students', '0025_rename_create_package_student_select_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='badge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_gamification.badge'),
        ),
    ]
