# Generated by Django 2.2 on 2020-06-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200626_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_background_picture',
            field=models.ImageField(default='profile_background_picture/banner.jpg', upload_to='profile_background_picture'),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(default='profile_picture/pic.png', upload_to='profile_picture'),
        ),
    ]