# Generated by Django 3.2.7 on 2021-09-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='Lprice',
            field=models.CharField(default=50000, max_length=10),
            preserve_default=False,
        ),
    ]