# Generated by Django 4.2 on 2024-01-24 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0033_alter_batch_add_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_title', models.CharField(max_length=255)),
                ('meeting_description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('zoom_meeting_id', models.CharField(blank=True, max_length=100, null=True)),
                ('zoom_meeting_password', models.CharField(blank=True, max_length=100)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.batch')),
            ],
        ),
    ]
