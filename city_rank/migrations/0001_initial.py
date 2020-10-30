# Generated by Django 3.1.2 on 2020-10-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='city_images/%Y/%m/%d', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='CityParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=100)),
                ('value', models.SmallIntegerField()),
                ('period', models.DateField(verbose_name='Период')),
            ],
            options={
                'verbose_name': 'Параметр города',
                'verbose_name_plural': 'Параметры города',
            },
        ),
    ]
