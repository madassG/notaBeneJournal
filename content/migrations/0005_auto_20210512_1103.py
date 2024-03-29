# Generated by Django 3.2.2 on 2021-05-12 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_post_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=150, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 12, 11, 3, 45, 60714), verbose_name='Время публикации'),
        ),
    ]
