# Generated by Django 3.0 on 2020-01-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20191203_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2020-01-08'),
        ),
    ]
