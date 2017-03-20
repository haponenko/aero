# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date_out', models.DateField()),
                ('date_in', models.DateField()),
                ('country_out', models.CharField(max_length=30)),
                ('city_out', models.CharField(max_length=30)),
                ('country_in', models.CharField(max_length=30)),
                ('city_in', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
