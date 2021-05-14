from django.contrib import admin
from . import models


@admin.register(models.Event)
class SubscribePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'video', 'date']


@admin.register(models.Member)
class SubscribePageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']
