# Generated by Django 3.2.4 on 2021-06-30 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokefriend', '0002_alter_trainer_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
