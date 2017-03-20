# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date_in', models.DateTimeField()),
                ('date_out', models.DateTimeField()),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
