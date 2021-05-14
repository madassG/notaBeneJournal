from django.shortcuts import render
from django.utils import timezone
from content.models import Type, Category, Post, Serie, rate_post
from .models import Event
from .forms import MemberForm
import datetime


def navigation():
    types = Type.objects.all()
    for typ in types:
        cats = Category.objects.filter(type=typ)
        typ.cats = cats
    return types


def index(request):
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
        'events': events,
    })


def about(request):
    nav = navigation()
    return render(request, 'about.html', {
        'nav': nav,
    })


def enter(request):
    success = False
    nav = navigation()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = MemberForm()
    return render(request, 'enter.html', {
        'nav': nav,
        'form': form,
        'success': success
    })


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
