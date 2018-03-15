# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180120_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(choices=[('no', 'Без породы'), ('1', 'Русская голубая'), ('2', 'Персидская кошка')], default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(choices=[('no', 'Без породы'), ('1', 'Немечкая овчарка'), ('2', 'Ёкширский терьер')], default=None, max_length=4),
        ),
    ]
