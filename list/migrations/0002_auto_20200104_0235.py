# Generated by Django 3.0 on 2020-01-03 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 4, 2, 35, 49, 95251)),
        ),
    ]
