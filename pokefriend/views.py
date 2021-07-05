from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone

from pokefriend.forms import TrainerRegisterForms, TrainerSearchForms
from pokefriend.models import Trainer


def index(request):
    register_form = TrainerRegisterForms()
    search_form = TrainerSearchForms()
    trainers = Trainer.objects.all()
    if request.method == 'POST':
        form = TrainerRegisterForms(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            team = form.cleaned_data.get('team')
            country = form.cleaned_data.get('country')
            trainer = Trainer.objects.filter(code=code).first()
            if trainer:
                trainer.last_modified = timezone.now()
                trainer.country = country
                trainer.team = team
                trainer.save()
            else:
                form.save()
            trainers = Trainer.objects.all()
            form = TrainerRegisterForms()

        context = {
            'register_form': form,
            'search_form': search_form,
            'trainers': trainers,
        }
        return render(request, 'index.html', context)
    context = {
        'register_form': register_form,
        'search_form': search_form,
        'trainers': trainers,
    }
    return render(request, 'index.html', context)


def search(request):
    register_form = TrainerRegisterForms()
    search_form = TrainerSearchForms(request.GET)
    trainers = None

    query = Q()
    if search_form.is_valid():
        country = search_form.cleaned_data.get('country')
        team = search_form.cleaned_data.get('team')
        if country:
            query &= Q(country=country)
        if team:
            if team != 'ANY':
                query &= Q(team=team)
        trainers = Trainer.objects.filter(query)

    context = {
        'register_form': register_form,
        'search_form': search_form,
        'trainers': trainers,
    }
    return render(request, 'index.html', context)


def faq(request):
    return render(request, 'faq.html')
