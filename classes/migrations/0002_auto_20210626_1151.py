# Generated by Django 3.1.2 on 2021-06-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclass',
            name='title',
            field=models.CharField(default='Class', max_length=150),
        ),
    ]
