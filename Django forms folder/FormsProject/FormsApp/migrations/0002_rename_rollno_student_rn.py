# Generated by Django 3.2.7 on 2021-09-09 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='rollno',
            new_name='rn',
        ),
    ]
