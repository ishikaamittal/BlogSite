# Generated by Django 3.2.7 on 2022-02-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_postblog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='blog_image',
            field=models.ImageField(default='blog_default.jpg', upload_to='blog_image'),
        ),
    ]
