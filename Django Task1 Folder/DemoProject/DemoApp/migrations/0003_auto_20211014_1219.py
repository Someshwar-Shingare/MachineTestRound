# Generated by Django 3.2.8 on 2021-10-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0002_auto_20211014_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]