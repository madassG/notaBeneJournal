from django.shortcuts import render
from django.utils import timezone
from content.models import Type, Category, Post, Serie, rate_post
from .models import Event
from .forms import MemberForm, MailingForm
import datetime


def navigation():
    types = Type.objects.all()
    for typ in types:
        cats = Category.objects.filter(type=typ)
        typ.cats = cats
    return types


def index(request):
    form = MailingForm()
    success = False
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    nav = navigation()
    types = Type.objects.all()
    for typ in types:
        typ.count = 0
        for cat in typ.categories.all():
            typ.count += cat.posts.filter(show=True).count()

    events = Event.objects.filter(date__gte=datetime.datetime.now())
    return render(request, 'index.html', {
        'nav': nav,
        'headings': types,
        'emailForm': form,
        'events': events,
        'success': success,
    })


def about(request):
    form = MailingForm()
    success = False
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    nav = navigation()
    return render(request, 'about.html', {
        'nav': nav,
        'success': success,
        'emailForm': form,
    })


def enter(request):
    memberSuccess = False
    nav = navigation()
    emailForm = MailingForm()
    success = False
    if request.method == 'POST' and 'emailForm' in request.POST:
        emailForm = MailingForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            success = True
    if request.method == 'POST' and 'memberForm' in request.POST:
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            memberSuccess = True
    else:
        form = MemberForm()
    return render(request, 'enter.html', {
        'nav': nav,
        'memberForm': form,
        'memberSuccess': memberSuccess,
        'success': success,
        'emailForm': emailForm,
    })


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
