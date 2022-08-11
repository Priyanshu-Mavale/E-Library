# Generated by Django 4.0.3 on 2022-04-27 18:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0014_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='PublishedIn',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_uploaded',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]