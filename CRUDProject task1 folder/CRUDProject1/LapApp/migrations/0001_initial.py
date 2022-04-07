# Generated by Django 3.2.7 on 2021-09-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=32)),
                ('model_name', models.CharField(max_length=32)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('ssd', models.IntegerField()),
                ('processor', models.CharField(max_length=30)),
                ('os', models.CharField(max_length=32)),
                ('price', models.FloatField(max_length=32)),
            ],
        ),
    ]
