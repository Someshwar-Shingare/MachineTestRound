# Generated by Django 4.0.3 on 2022-04-07 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_author_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
    ]
