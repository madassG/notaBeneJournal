from django.conf.urls import handler404, handler500
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, Http404
from django.core.paginator import Paginator
from django.shortcuts import render
from django import forms
from main.forms import MailingForm
from .models import Type, Category, Post, Serie, rate_post
from .forms import RateForm
import main


handler404 = main.views.handler404
handler500 = main.views.handler500


def navigation():
    types = Type.objects.all()
    for typ in types:
        cats = Category.objects.filter(type=typ)
        typ.cats = cats
    return types


def type_view(request, type):
    emailForm = MailingForm()
    success = False
    if request.method == 'POST':
        emailForm = MailingForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            success = True
    nav = navigation()
    type = get_object_or_404(Type, name=type.lower())
    categories = Category.objects.filter(type=type)
    posts = Post.objects.filter(category__in=categories).filter(show=True).order_by('-published_at')
    items = Paginator(posts, 6)
    return render(request, 'content/tiles.html', {
        'nav': nav,
        'items': items,
        'type': type,
        'emailForm': emailForm,
        'success': success,
    })


def category_view(request, type, category):
    nav = navigation()
    emailForm = MailingForm()
    success = False
    if request.method == 'POST':
        emailForm = MailingForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            success = True
    type = get_object_or_404(Type, name=type.lower())
    cat = Category.objects.filter(slug=category.lower()).filter(type=type)
    if not cat:
        raise Http404()

    posts = Post.objects.filter(category=cat[0]).order_by('-published_at')
    items = Paginator(posts, 6)
    return render(request, 'content/category.html', {
        'nav': nav,
        'items': items,
        'cat': cat[0],
        'emailForm': emailForm,
        'success': success,
    })


def post_page(request, type, category, post):
    nav = navigation()
    type = get_object_or_404(Type, name=type.lower())
    cat = Category.objects.filter(slug=category.lower()).filter(type=type)
    if not cat:
        raise Http404()
    posts = Post.objects.filter(category=cat[0]).filter(show=True).filter(slug=post.lower())
    if not posts:
        raise Http404()
    post = posts[0]
    emailForm = MailingForm()
    success = False

    if request.method == 'POST' and 'emailForm' in request.POST:
        emailForm = MailingForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            success = True
    if request.method == 'POST' and 'rateForm' in request.POST:
        rated = request.POST.get('rate', None)
        form = RateForm(request.POST)
        if rated:
            rates = rate_post.objects.filter(post=post).filter(ip=request.META.get('REMOTE_ADDR'))
            if rates:
                form.errors['rate'] = {'message': 'Вы уже проголосовали', 'code': 'not_allowed'}
            else:
                rate = rate_post()
                rate.post = post
                rate.rate = rated
                rate.ip = request.META.get('REMOTE_ADDR')
                setattr(post, rated, getattr(post, rated)+1)
                post.save()
                rate.save()
    else:
        form = RateForm()
    rated = False
    rates = rate_post.objects.filter(post=post).filter(ip=request.META.get('REMOTE_ADDR'))
    if rates:
        rated = True

    similar = []
    similar += Post.objects.filter(category=cat[0]).exclude(slug=post.slug)
    similar += Post.objects.exclude(category=cat[0])
    return render(request, 'content/post.html', {
        'nav': nav,
        'post': post,
        'rateForm': form,
        'emailForm': emailForm,
        'success': success,
        'rated': rated,
        'similar': similar[:3],
    })


def series(request):
    emailForm = MailingForm()
    success = False
    if request.method == 'POST':
        emailForm = MailingForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            success = True
    nav = navigation()
    sers = Serie.objects.filter(show=True).order_by('-published_at')
    items = Paginator(sers, 4)
    return render(request, 'content/series.html', {
        'nav': nav,
        'items': items,
        'emailForm': emailForm,
        'success': success,
    })


def serie_view(request, serie):
    emailForm = MailingForm()
    success = False
    if request.method == 'POST':
        emailForm = MailingForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            success = True
    nav = navigation()
    serie = get_object_or_404(Serie, slug=serie.lower())
    posts_raw = serie.posts.through.objects.all()
    posts = []
    for post in posts_raw:
        if post.post.show:
            posts.append(post.post)
    items = Paginator(posts, 2)
    return render(request, 'content/serie.html', {
        'nav': nav,
        'serie': serie,
        'items': items,
        'emailForm': emailForm,
        'success': success,
    })


def serie_post(request, serie, post):
    nav = navigation()
    serie = get_object_or_404(Serie, slug=serie.lower())
    posts_raw = serie.posts.through.objects.all()
    postt = None
    similar = []
    slugs = []

    for p in posts_raw:
        if p.post.show and p.post.slug == post.lower():
            postt = p.post
        if p.post.show and p.post.slug != post.lower():
            similar.append(p.post)
            slugs.append(p.post.slug)
    if not postt:
        raise Http404
    similar += Post.objects.filter(category=postt.category).exclude(slug__in=slugs)
    if len(similar) < 3:
        similar += Post.objects.exclude(id=postt.pk).exclude(category=postt.category)
    similar = similar[:3]
    emailForm = MailingForm()
    success = False

    if request.method == 'POST' and 'emailForm' in request.POST:
        emailForm = MailingForm(request.POST)
        if emailForm.is_valid():
            emailForm.save()
            success = True
    form = RateForm()
    if request.method == 'POST' and 'rateForm':
        rated = request.POST.get('rate', None)
        if rated:
            rates = rate_post.objects.filter(post=postt).filter(ip=request.META.get('REMOTE_ADDR'))
            if rates:
                form.errors['rate'] = {'message': 'Вы уже проголосовали', 'code': 'not_allowed'}
            rate = rate_post()
            rate.post = postt
            rate.rate = rated
            rate.ip = request.META.get('REMOTE_ADDR')
            setattr(postt, rated, getattr(postt, rated)+1)
            postt.save()
            rate.save()
    rated = False
    rates = rate_post.objects.filter(post=postt).filter(ip=request.META.get('REMOTE_ADDR'))
    if rates:
        rated = True
    return render(request, 'content/post.html', {
        'nav': nav,
        'serie': serie,
        'post': postt,
        'rateForm': form,
        'emailForm': emailForm,
        'success': success,
        'rated': rated,
        'similar': similar,
    })
