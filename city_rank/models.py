from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

import datetime


class Person(models.Model):
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    position = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_person")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Позьзователь"
        verbose_name_plural = "Пользователи"


class CityParams(models.Model):
    """Параметры"""
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    value = models.SmallIntegerField()
    period = models.DateField("Период")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Параметр города'
        verbose_name_plural = 'Параметры города'


class Event(models.Model):
    """Мероприятие"""
    status_choices = [
        ('GO', 'Выполняется'),
        ('EN', 'Завершена'),
        ('FA', 'Провалена'),
    ]

    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=30)
    accountable = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.CharField(max_length=2,
                              choices=status_choices,
                              default='GO')
    description = models.TextField()
    target = models.ForeignKey(CityParams, on_delete=models.CASCADE)

    def days_left(self):
        return (self.date_end - datetime.date.today()).days

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Task(models.Model):
    """Задача"""
    status_choices = [
        ('GO', 'Выполняется'),
        ('EN', 'Завершена'),
        ('FA', 'Провалена'),
    ]

    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField("Осталось")
    name = models.CharField("Название", max_length=30)
    accountable = models.ForeignKey(Person, verbose_name="Исполнитель", on_delete=models.CASCADE)
    status = models.CharField(max_length=2,
                              choices=status_choices,
                              default='GO')
    description = models.TextField("Описание")

    def days_left(self):
        return (self.date_end - datetime.date.today()).days

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Token(models.Model):
    """Токен"""
    value = models.CharField(max_length=32)
    ttl = models.DateField()

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Токен"
        verbose_name_plural = "Токены"


class ExternalUser(models.Model):
    """Внешний пользователь"""
    name = models.CharField(max_length=30)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ExternalQuery(models.Model):
    """Внешний запрос"""
    text = models.TextField(max_length=30)
    external_user = models.ForeignKey(ExternalUser, on_delete=models.CASCADE)
    city_params = models.ForeignKey(CityParams, on_delete=models.CASCADE)

    def __str__(self):
        return self.external_user.name

    class Meta:
        verbose_name = "Внешний запрос"
        verbose_name_plural = "Внешние запросы"


class City(models.Model):
    """Город"""
    city_scales = [
        ('крупнейшие города с численностью населения от 1 млн. человек', '(01) крупнейшие города с численностью населения от 1 млн. человек'),
        ('крупные города с численностью населения от 250 тыс. до 1 млн. человек', '(02) крупные города с численностью населения от 250 тыс. до 1 млн. человек'),
        ('большие города с численностью населения от 100 тыс. до 250 тыс. человек', '(03) большие города с численностью населения от 100 тыс. до 250 тыс. человек'),
        ('средние города с численностью населения от 50 тыс. до 100 тыс. человек', '(04) средние города с численностью населения от 50 тыс. до 100 тыс. человек'),
        ('малые города с численностью населения от 25 тыс. до 50 тыс. человек', '(05) малые города с численностью населения от 25 тыс. до 50 тыс. человек'),
        ('малые города с численностью населения от 5 тыс. до 25 тыс. человек', '(06) малые города с численностью населения от 5 тыс. до 25 тыс. человек'),
        ('малые города с численностью населения до 5 тыс. человек', '(07) малые города с численностью населения до 5 тыс. человек'),
        ('крупные и большие города с численностью населения от 100 тыс. до 1 млн. человек', '(08) крупные и большие города с численностью населения от 100 тыс. до 1 млн. человек'),
        ('средние и малые города с численностью населения от 25 тыс. до 100 тыс. человек', '(09) средние и малые города с численностью населения от 25 тыс. до 100 тыс. человек'),
        ('малые города с численностью населения до 25 тыс. человек', '(10) малые города с численностью населения до 25 тыс. человек'),
    ]

    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    city_scale = models.CharField(max_length=100,
                                  choices=city_scales,
                                  default='малые города с численностью населения до 25 тыс. человек')

    def get_absolute_url(self):
        return reverse('main_detail', args=[self.pk])

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

