# Generated by Django 4.2 on 2024-01-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0015_package_user_package'),
        ('students', '0022_alter_student_create_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='create_package',
            field=models.ManyToManyField(blank=True, null=True, to='package.package'),
        ),
    ]
