# Generated by Django 3.2.6 on 2021-08-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название Биржи')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('currency', models.CharField(max_length=10, verbose_name='Валюта')),
                ('price', models.FloatField(default=2, verbose_name='Цена')),
            ],
        ),
    ]
