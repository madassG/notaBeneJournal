# Generated by Django 3.2.2 on 2021-05-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_type_name_ru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name_ru',
            field=models.CharField(max_length=100, unique=True, verbose_name='Русское название'),
        ),
    ]