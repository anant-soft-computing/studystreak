# Generated by Django 5.0 on 2023-12-11 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0001_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=255)),
                ('package_price', models.CharField(max_length=100)),
                ('soft_copy', models.BooleanField(default=False)),
                ('hard_copy', models.BooleanField(default=False)),
                ('full_length_test', models.BooleanField(default=False)),
                ('practice_test', models.BooleanField(default=False)),
                ('speaking_test', models.BooleanField(default=False)),
                ('writing_evaluation', models.BooleanField(default=False)),
                ('Total_test', models.IntegerField(default=10)),
                ('live_classes_membership', models.BooleanField(default=False)),
                ('online_membership', models.BooleanField(default=False)),
                ('offline_membership', models.BooleanField(default=False)),
                ('group_doubt_solving', models.BooleanField(default=False)),
                ('one_to_one_doubt_solving', models.BooleanField(default=False)),
                ('PackageType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.packagetype')),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course')),
            ],
        ),
    ]
