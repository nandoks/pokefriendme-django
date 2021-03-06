# Generated by Django 3.2.4 on 2021-06-30 16:08

import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('last_modified', models.DateTimeField(default=datetime.datetime(2021, 6, 30, 13, 8, 54, 272332))),
                ('team', models.CharField(choices=[('MYSTIC', 'Mystic'), ('VALOR', 'Valor'), ('INSTINCT', 'Instinct'), ('ANY', 'Any')], default='ANY', max_length=10)),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
    ]
