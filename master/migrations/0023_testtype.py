# Generated by Django 4.2 on 2023-12-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0022_moduletype'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]