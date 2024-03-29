# Generated by Django 4.2 on 2024-02-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0002_initial'),
        ('package', '0001_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='add_package',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='package.package'),
        ),
        migrations.AddField(
            model_name='additionalresource',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course'),
        ),
    ]
