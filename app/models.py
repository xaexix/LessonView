from django.db import models

# Create your models here.
# Биржа Дата Время Валюта Цена Изменение Изменение, % Макс. Мин.

class Stock(models.Model):
    name = models.CharField(verbose_name='Название Биржи', max_length=50)
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    currency = models.CharField(verbose_name='Валюта', max_length=10)
    price = models.FloatField(verbose_name='Цена', default=2)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Акции'
        verbose_name_plural = 'Акции'
