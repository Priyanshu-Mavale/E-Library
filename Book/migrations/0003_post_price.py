# Generated by Django 4.0.3 on 2022-03-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_post_file_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Price',
            field=models.IntegerField(default=0),
        ),
    ]
