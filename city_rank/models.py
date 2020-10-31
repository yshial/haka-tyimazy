from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class CityParams(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    value = models.SmallIntegerField()
    period = models.DateField("Период")


def __str__(self):
    return "{}".format(self.code)


def parse(self):
    pass


class Meta:
    verbose_name = 'Параметр города'
    verbose_name_plural = 'Параметры города'


class City(models.Model):
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("Изображение",
                              upload_to='city_images/%Y/%m/%d')
    description = models.TextField("Описание")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


# class Tasks(models.Model):
#     name = models.CharField("Наименование", max_length=100),
#     responsible = models.ForeignKey(User,
#                                     on_delete=models.CASCADE,
#                                     verbose_name="Ответственный",
#                                     related_name="res")
#     term = models.DateField("Срок")
#     is_completed = models.BooleanField("Завершен", default=False)
#
#     def __str__(self):
#         return "{}".format(self.name)
#
#     class Meta:
#         verbose_name = "Задача"
#         verbose_name_plural = "Задачи"
#
#
# class Activity(models.Model):
#     description = models.TextField("Описание")
#     target = models.
