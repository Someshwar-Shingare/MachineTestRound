# Generated by Django 3.2.8 on 2021-10-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthify', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
