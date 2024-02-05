# Generated by Django 4.2 on 2024-02-05 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses', '0001_initial'),
        ('coursedetail', '0002_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.category'),
        ),
        migrations.AddField(
            model_name='course',
            name='Language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.language'),
        ),
        migrations.AddField(
            model_name='course',
            name='Level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.level'),
        ),
        migrations.AddField(
            model_name='course',
            name='Outcome',
            field=models.ManyToManyField(to='master.outcomes'),
        ),
        migrations.AddField(
            model_name='course',
            name='Requirements',
            field=models.ManyToManyField(to='master.requirements'),
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(blank=True, to='coursedetail.lesson'),
        ),
        migrations.AddField(
            model_name='course',
            name='primary_instructor',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Instructor'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'Tutor'}, related_name='tutor', to=settings.AUTH_USER_MODEL),
        ),
    ]