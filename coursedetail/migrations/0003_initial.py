# Generated by Django 4.2 on 2024-02-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coursedetail', '0002_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='section',
            field=models.ForeignKey(blank=True, default=None, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.section'),
        ),
    ]