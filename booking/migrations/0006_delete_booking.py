# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
