from django.db import models
from django_countries.fields import CountryField

from datetime import datetime
from django.utils import timezone


class Trainer(models.Model):
    code = models.CharField(max_length=12)
    country = CountryField(blank_label='World Wide', blank=True)
    last_modified = models.DateTimeField(default=timezone.now)

    class Team(models.TextChoices):
        ANY = 'ANY'
        MYSTIC = 'MYSTIC'
        VALOR = 'VALOR'
        INSTINCT = 'INSTINCT'

    team = models.CharField(max_length=10, choices=Team.choices, default=Team.ANY)

    class Meta:
        ordering = ['-last_modified']

    def __str__(self):
        return self.code
