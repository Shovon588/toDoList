# Generated by Django 3.0.4 on 2020-04-17 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_auto_20200104_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 1, 57, 48, 985055)),
        ),
    ]
