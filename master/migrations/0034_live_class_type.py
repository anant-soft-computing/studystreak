# Generated by Django 4.2 on 2024-01-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0033_alter_batch_add_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live_Class_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]