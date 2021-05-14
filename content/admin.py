from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from . import models


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget)

    class Meta:
        model = models.Post
        fields = '__all__'


class SerieAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget)

    class Meta:
        model = models.Serie
        fields = '__all__'


@admin.register(models.Type)
class SubscribePageAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_ru']
    search_fields = ['name', 'name_ru']


@admin.register(models.Category)
class SubscribePageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'type']
    search_fields = ['name', 'type']
    list_filter = ('type', )


@admin.register(models.Post)
class SubscribePageAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'subtitle', 'content', 'author', 'editor', 'tags', 'sources', 'show']
    readonly_fields = ('useful', 'want_more', 'share', 'curious', 'published_at')
    search_fields = ['title', 'tags', 'subtitle', 'content', 'author', 'editor']
    list_filter = ('show', 'category')
    form = PostAdminForm


@admin.register(models.Serie)
class SubscribePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image', 'content', 'show']
    readonly_fields = ('published_at', )
    search_fields = ['title', 'subtitle', 'content']
    list_filter = ('show', )

    filter_horizontal = ('posts',)
    form = PostAdminForm
