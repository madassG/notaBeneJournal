# Generated by Django 3.2.2 on 2021-05-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_serie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='curious',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='share',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='useful',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='want_more',
            field=models.IntegerField(default=0),
        ),
    ]
