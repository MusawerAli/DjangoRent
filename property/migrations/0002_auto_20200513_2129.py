# Generated by Django 3.0.6 on 2020-05-13 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberdetail',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='memberdetail',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 21, 29, 7, 632284)),
        ),
    ]
