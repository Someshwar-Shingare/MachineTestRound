# Generated by Django 3.2.7 on 2021-09-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rn', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('marks', models.FloatField()),
            ],
        ),
    ]
