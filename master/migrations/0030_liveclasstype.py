# Generated by Django 4.2 on 2024-01-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0029_coursematerial_material_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveClassType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
