from datetime import datetime, timedelta

from .models import Trainer
from django.utils import timezone


def code_has_twelve_numbers(code, label, error_list):
    if not code.isdecimal():
        error_list[label] = f'Trainer code must only contain digits'
    if len(code) != 12:
        error_list[label] = f'Trainer coe must contain 12 digits with 0 or 2 spaces.'


def code_entered_24h_or_more(code, label, error_list):
    trainer = Trainer.objects.filter(code=code).first()
    if trainer:
        if trainer.last_modified.__gt__(timezone.now() - timezone.timedelta(hours=24)):
            error_list[label] = f'Trainer code entered less than 24h ago. Please wait 24h before resending trainer code'
