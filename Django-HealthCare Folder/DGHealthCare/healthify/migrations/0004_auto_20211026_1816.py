# Generated by Django 3.2.8 on 2021-10-26 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthify', '0003_doctor_nursingstaff_roomservicestaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(choices=[('BHMS', 'BHMS'), ('BAMS', 'BAMS'), ('MBBS', 'MBBS'), ('Physiotherapists', 'Physiotherapists'), ('MD', 'MD')], max_length=50),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='healthify.category')),
            ],
        ),
    ]
