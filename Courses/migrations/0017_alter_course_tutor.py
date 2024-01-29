# Generated by Django 4.2 on 2024-01-29 13:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses', '0016_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tutor',
            field=models.ManyToManyField(related_name='tutor', to=settings.AUTH_USER_MODEL),
        ),
    ]
