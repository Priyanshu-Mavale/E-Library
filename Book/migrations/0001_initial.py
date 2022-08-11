# Generated by Django 4.0.3 on 2022-03-22 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=50)),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('Info', models.CharField(max_length=1000)),
                ('Genre', models.CharField(max_length=30)),
                ('Uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]