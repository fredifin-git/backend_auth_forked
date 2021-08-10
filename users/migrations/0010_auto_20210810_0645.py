# Generated by Django 3.1.2 on 2021-08-10 06:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210810_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='improvablepoints',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0), blank=True, default=1, size=26),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='strongpoints',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=1), blank=True, default=1, size=28),
        ),
    ]
