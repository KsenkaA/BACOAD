# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20180123_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='photo',
            field=models.ImageField(default='..defaultpic.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='photo',
            field=models.ImageField(default='..defaultpic.png', upload_to='media/'),
        ),
    ]
