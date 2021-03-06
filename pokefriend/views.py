from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
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
            code = form.cleaned_data.get('code').replace(' ', '')
            team = form.cleaned_data.get('team')
            country = form.cleaned_data.get('country')
            trainer = Trainer.objects.filter(code=code).first()
            if trainer:
                trainer.last_modified = timezone.now()
                trainer.country = country
                trainer.team = team
                trainer.save()
            else:
                trainer = form.save(commit=False)
                trainer.code = code
                trainer.save()
            trainers = Trainer.objects.all()
            form = TrainerRegisterForms()
        paginator = Paginator(trainers, 9)
        trainer_page_object = paginator.get_page(1)
        context = {
            'register_form': form,
            'search_form': search_form,
            'trainers': trainer_page_object,
        }
        return render(request, 'index.html', context)
    paginator = Paginator(trainers, 9)
    page_number = request.GET.get('page') if request.GET.get('page') else 1
    trainer_page_object = paginator.get_page(page_number)
    context = {
        'register_form': register_form,
        'search_form': search_form,
        'trainers': trainer_page_object,
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
