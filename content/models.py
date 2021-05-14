from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Type(models.Model):
    def __str__(self):
        return self.name_ru
    name = models.CharField(max_length=100, verbose_name='Тип', unique=True)
    description = models.TextField(max_length=500, verbose_name='Описание', blank=True)
    name_ru = models.CharField(max_length=100, verbose_name='Русское название', unique=True)


class Category(models.Model):
    def __str__(self):
        return self.name
    slug = models.CharField(max_length=150, verbose_name='Слаг')
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='contentImages/category', max_length=800, verbose_name='Превью категории')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories', verbose_name='Тип категории')


class Post(models.Model):
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.show:
            self.published_at = timezone.now()
        super(Post, self).save(*args, **kwargs)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts',
                                 verbose_name='Категория поста', null='True')
    slug = models.CharField(max_length=100, verbose_name='Слаг', unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    subtitle = models.TextField(max_length=500, blank=True, verbose_name='Подзаголовок')
    content = RichTextField(verbose_name='Контент')
    author = models.CharField(max_length=200, verbose_name='Автор')
    editor = models.CharField(max_length=200, blank=True, verbose_name='Редактор')
    tags = models.TextField(max_length=1500, blank=True, verbose_name='Теги')
    sources = models.TextField(max_length=500, blank=True, verbose_name='Источники')
    show = models.BooleanField(default=False, verbose_name='Показывать?')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')

    useful = models.IntegerField(default=0)
    want_more = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    curious = models.IntegerField(default=0)


class Serie(models.Model):
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.show:
            self.published_at = timezone.now()
        super(Serie, self).save(*args, **kwargs)

    slug = models.CharField(max_length=100, verbose_name='Слаг', unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    subtitle = models.TextField(max_length=500, blank=True, verbose_name='Подзаголовок')
    image = models.ImageField(upload_to='contentImages/series', max_length=800, verbose_name='Превью серии')
    content = RichTextField(verbose_name='Контент')
    posts = models.ManyToManyField(Post)
    show = models.BooleanField(default=False, verbose_name='Показывать?')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')


class serie_post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='series_links', verbose_name='Пост')
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='posts_links', verbose_name='Серия')


class rate_post(models.Model):
    CHOICES = (
        ('useful', 'Полезно!'),
        ('want_more', 'Интересная статья, хочу больше таких!'),
        ('share', 'Поделюсь с друзьями!'),
        ('curious', 'Любопытно!')
    )
    ip = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='rate', verbose_name='Пост')
    rate = models.CharField(max_length=100, choices=CHOICES)
