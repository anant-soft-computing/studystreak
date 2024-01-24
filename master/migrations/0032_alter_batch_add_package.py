# Generated by Django 4.2 on 2024-01-24 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0017_alter_package_package_name'),
        ('master', '0031_alter_lessonassignment_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='add_package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='package.package'),
            preserve_default=False,
        ),
    ]
