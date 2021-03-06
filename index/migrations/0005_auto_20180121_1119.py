# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180120_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.CharField(choices=[('не указан', 'не указан'), ('заводчик', 'заводчик'), ('приют', 'приют')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='cat',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cat',
            name='sex',
            field=models.CharField(choices=[('не указан', 'не указан'), ('мальчик', 'мальчик'), ('девочка', 'девочка')], default='не указан', max_length=6),
        ),
        migrations.AlterField(
            model_name='cat',
            name='size',
            field=models.CharField(choices=[('не указан', 'не указан'), ('маленький', 'маленький'), ('средний', 'средний'), ('большой', 'большой')], default='не указан', max_length=10),
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.CharField(choices=[('не указан', 'не указан'), ('заводчик', 'заводчик'), ('приют', 'приют')], default='не указан', max_length=10),
        ),
        migrations.AlterField(
            model_name='dog',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dog',
            name='sex',
            field=models.CharField(choices=[('не указан', 'не указан'), ('мальчик', 'мальчик'), ('девочка', 'девочка')], default='не указан', max_length=6),
        ),
        migrations.AlterField(
            model_name='dog',
            name='size',
            field=models.CharField(choices=[('не указан', 'не указан'), ('маленький', 'маленький'), ('средний', 'средний'), ('большой', 'большой')], default='не указан', max_length=10),
        ),
    ]
