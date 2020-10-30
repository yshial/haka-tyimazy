from django.db import models

ParamsTemplate = [
    ('1', 'Param1'),
    ('2', 'Param2'),
    ('3', 'Param3'),
    ('4', 'Param4'),
    ('5', 'Param5'),
    ('6', 'Param6'),
    ('7', 'Param7'),
    ('8', 'Param8'),
    ('9', 'Param9'),
    ('10', 'Param10'),
    ('11', 'Param11'),
    ('12', 'Param12'),
    ('13', 'Param13'),
    ('14', 'Param14'),
    ('15', 'Param15'),
    ('16', 'Param16'),
    ('17', 'Param17'),
    ('18', 'Param18'),
    ('19', 'Param19'),
    ('20', 'Param20'),
    ('21', 'Param21'),
    ('22', 'Param22'),
    ('23', 'Param23'),
    ('24', 'Param24'),
    ('25', 'Param25'),
    ('26', 'Param26'),
    ('27', 'Param27'),
    ('28', 'Param28'),
    ('29', 'Param29'),
    ('30', 'Param30'),
    ('31', 'Param31'),
    ('32', 'Param32'),
    ('33', 'Param33'),
    ('34', 'Param34'),
    ('35', 'Param35'),
    ('36', 'Param36'),
]


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
