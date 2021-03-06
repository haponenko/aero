# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 19:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20160112_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='region_in',
            new_name='state_in',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='region_out',
            new_name='state_out',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_in',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_out',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
