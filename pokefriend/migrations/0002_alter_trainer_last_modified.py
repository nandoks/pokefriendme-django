# Generated by Django 3.2.4 on 2021-06-30 16:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokefriend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 30, 16, 40, 49, 260889, tzinfo=utc)),
        ),
    ]
