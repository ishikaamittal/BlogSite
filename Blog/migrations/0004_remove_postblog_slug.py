# Generated by Django 4.0.1 on 2022-01-27 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_postblog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postblog',
            name='slug',
        ),
    ]
