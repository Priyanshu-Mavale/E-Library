# Generated by Django 4.0.3 on 2022-04-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.TextField(max_length=30)),
                ('bauthor', models.TextField(max_length=30)),
                ('bgenre', models.TextField(max_length=30)),
                ('bpreface', models.TextField()),
                ('bfile', models.FileField(default='download.jpg', upload_to='static/')),
            ],
        ),
    ]
