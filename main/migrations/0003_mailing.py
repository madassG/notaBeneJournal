# Generated by Django 3.2.2 on 2021-05-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
        ),
    ]
