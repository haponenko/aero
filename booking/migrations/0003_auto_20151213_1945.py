# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20151213_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='city_in',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='city_out',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='country_in',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='country_out',
            field=models.CharField(default='', max_length=30),
        ),
    ]