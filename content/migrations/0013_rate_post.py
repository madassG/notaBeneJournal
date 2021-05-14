# Generated by Django 3.2.2 on 2021-05-13 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20210514_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='rate_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200)),
                ('rate', models.CharField(choices=[('useful', 'Полезно!'), ('want_more', 'Интересная статья, хочу больше таких!'), ('share', 'Поделюсь с друзьями!'), ('curious', 'Любопытно!')], max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='content.post', verbose_name='Пост')),
            ],
        ),
    ]