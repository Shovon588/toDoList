# Generated by Django 3.0.4 on 2020-04-17 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_auto_20200418_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 2, 8, 59, 343200)),
        ),
    ]
