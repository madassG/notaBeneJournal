# Generated by Django 3.2.2 on 2021-05-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('subtitle', models.TextField(max_length=600, verbose_name='Подзаголовок')),
                ('video', models.URLField(verbose_name='Ссылка youtube')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
        ),
    ]
