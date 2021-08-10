# Generated by Django 3.1.2 on 2021-08-10 06:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210810_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='improvablepoints',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=26),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='strongpoints',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=28),
        ),
    ]
