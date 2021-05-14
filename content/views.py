from django.conf.urls import handler404, handler500
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, Http404
from django.core.paginator import Paginator
from django.shortcuts import render
from django import forms
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
    nav = navigation()
    type = get_object_or_404(Type, name=type.lower())
    categories = Category.objects.filter(type=type)
    posts = Post.objects.filter(category__in=categories).filter(show=True).order_by('-published_at')
    items = Paginator(posts, 6)
    return render(request, 'content/tiles.html', {
        'nav': nav,
        'items': items,
        'type': type,
    })


def category_view(request, type, category):
    nav = navigation()
    type = get_object_or_404(Type, name=type.lower())
    cat = Category.objects.filter(slug=category.lower()).filter(type=type)
    if not cat:
        raise Http404()

    posts = Post.objects.filter(category=cat[0])
    items = Paginator(posts, 6)
    return render(request, 'content/tiles.html', {
        'nav': nav,
        'items': items,
        'cat': cat[0],
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
    if request.method == 'POST':
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

    return render(request, 'content/post.html', {
        'nav': nav,
        'post': post,
        'form': form,
        'rated': rated,
    })


def series(request):
    nav = navigation()
    sers = Serie.objects.filter(show=True)
    items = Paginator(sers, 4)
    return render(request, 'content/series.html', {
        'nav': nav,
        'items': items,
    })


def serie_view(request, serie):
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
    })


def serie_post(request, serie, post):
    nav = navigation()
    serie = get_object_or_404(Serie, slug=serie.lower())
    posts_raw = serie.posts.through.objects.all()
    postt = None

    for p in posts_raw:
        if p.post.show and p.post.slug == post.lower():
            postt = p.post
    if not postt:
        raise Http404
    if request.method == 'POST':
        rated = request.POST.get('rate', None)
        if rated:
            rates = rate_post.objects.filter(post=postt).filter(ip=request.META.get('REMOTE_ADDR'))
            if rates:
                raise forms.ValidationError('Вы уже голосовали')
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
    form = RateForm()
    return render(request, 'content/post.html', {
        'nav': nav,
        'serie': serie,
        'post': postt,
        'form': form,
        'rated': rated,
    })
