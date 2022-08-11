# Generated by Django 4.0.3 on 2022-04-09 10:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0005_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fav',
            field=models.ManyToManyField(related_name='fav', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Saved',
        ),
    ]