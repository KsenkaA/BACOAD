# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='dog',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]
