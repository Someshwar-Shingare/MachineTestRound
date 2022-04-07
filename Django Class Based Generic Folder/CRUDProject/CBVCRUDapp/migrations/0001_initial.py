# Generated by Django 3.2.7 on 2021-09-22 10:07

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
                ('company', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]