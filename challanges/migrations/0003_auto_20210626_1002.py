# Generated by Django 3.1.2 on 2021-06-26 10:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challanges', '0002_auto_20210626_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='challanges',
            name='students',
            field=models.ManyToManyField(related_name='student_challanges', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ChallangeStudent',
        ),
    ]
