# Generated by Django 3.1.2 on 2021-08-09 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challanges', '0005_auto_20210808_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challanges',
            name='Assigned_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 9, 5, 59, 27, 879432)),
        ),
    ]