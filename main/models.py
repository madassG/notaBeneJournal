from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    subtitle = models.TextField(max_length=600, verbose_name='Подзаголовок')
    video = models.URLField(verbose_name='Ссылка youtube')
    date = models.DateTimeField(verbose_name='Дата')


class Member(models.Model):
    name = models.CharField(max_length=400, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True)
    message = models.TextField(max_length=500, verbose_name='Сообщение', blank=True)


class Mailing(models.Model):
    email = models.EmailField(verbose_name='Почта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
