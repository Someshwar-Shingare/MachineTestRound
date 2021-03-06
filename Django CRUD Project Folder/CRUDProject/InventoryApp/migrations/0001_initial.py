# Generated by Django 3.2.7 on 2021-09-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
