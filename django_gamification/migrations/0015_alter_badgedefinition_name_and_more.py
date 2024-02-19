# Generated by Django 4.2 on 2024-01-26 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_gamification', '0014_alter_badge_id_alter_badge_next_badge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgedefinition',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='badgedefinition',
            name='next_badge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_gamification.badgedefinition'),
        ),
    ]